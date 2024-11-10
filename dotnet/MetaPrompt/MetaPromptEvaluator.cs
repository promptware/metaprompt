using MetaPrompt.Models;
using MetaPrompt.Services.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt
{
    public class MetaPromptEvaluator
    {
        private readonly ILLMService _llmService;

        public MetaPromptEvaluator(ILLMService llmService)
        {
            _llmService = llmService;
        }

        public async Task<string> EvaluateAsync(Dictionary<string, object> metaprompt, ConfigModel config)
        {
            var env = new EnvModel(config.Parameters);
            var runtime = new RuntimeModel(config, env);

            string result = "";
            await foreach (var chunk in EvalAst(metaprompt, config, env, runtime))
            {
                result += chunk;
            }
            return result;
        }

        private async IAsyncEnumerable<string> EvalAst(Dictionary<string, object> ast, ConfigModel config, EnvModel env, RuntimeModel runtime)
        {
            if (!ast.ContainsKey("type"))
            {
                throw new Exception("AST node does not contain 'type' key.");
            }

            if (ast["type"].ToString() == "text")
            {
                yield return ast["text"].ToString();
            }
            else if (ast["type"].ToString() == "metaprompt")
            {
                if (ast["exprs"] is List<Dictionary<string, object>> exprsList)
                {
                    foreach (var expr in exprsList)
                    {
                        await foreach (var chunk in EvalAst(expr, config, env, runtime))
                        {
                            yield return chunk;
                        }
                    }
                }
            }
            else if (ast["type"].ToString() == "exprs")
            {
                if (ast["exprs"] is List<Dictionary<string, object>> exprsList)
                {
                    foreach (var expr in exprsList)
                    {
                        await foreach (var chunk in EvalAst(expr, config, env, runtime))
                        {
                            yield return chunk;
                        }
                    }
                }
            }
            else if (ast["type"].ToString() == "var")
            {
                string value = runtime.Env.Get(ast["name"].ToString());
                if (value == null)
                {
                    throw new Exception($"Variable not found: {ast["name"]}");
                }
                yield return value;
            }
            else if (ast["type"].ToString() == "meta")
            {
                List<string> chunks = new List<string>();

                if (ast["exprs"] is List<Dictionary<string, object>> exprsList)
                {
                    foreach (var expr in exprsList)
                    {
                        await foreach (var chunk in EvalAst(expr, config, env, runtime))
                        {
                            chunks.Add(chunk);
                        }
                    }
                }

                string metaPrompt = string.Join("", chunks);
                string output = await _llmService.GetResponseAsync("", metaPrompt);
                yield return output;
            }
            else if (ast["type"].ToString() == "if_then_else")
            {
                List<string> conditionChunks = new List<string>();

                if (ast["condition"] is List<Dictionary<string, object>> conditionExprs)
                {
                    foreach (var expr in conditionExprs)
                    {
                        await foreach (var chunk in EvalAst(expr, config, env, runtime))
                        {
                            conditionChunks.Add(chunk);
                        }
                    }
                }

                string condition = string.Join("", conditionChunks);

                string promptResult = "";
                int retries = 0;
                string systemPromt = "Please respond with either \"true\" or \"false\" only. No additional information or explanation is needed. Based on the statement provided, determine if it is true or false.";

                while (promptResult != "true" && promptResult != "false")
                {
                    if (retries > config.IfRetries)
                    {
                        throw new Exception($"Failed to determine condition after retries. \n systemPromt - {systemPromt} promt - {condition} result - {promptResult}");
                    }

                    promptResult = (await _llmService.GetResponseAsync(systemPromt, condition, 0)).Trim();

                    promptResult = promptResult.ToLower();

                    retries++;
                }

                if (promptResult == "true")
                {
                    if (ast["then"] is List<Dictionary<string, object>> thenExprsList)
                    {
                        foreach (var expr in thenExprsList)
                        {
                            await foreach (var chunk in EvalAst(expr, config, env, runtime))
                            {
                                yield return chunk;
                            }
                        }
                    }
                }
                else
                {
                    if (ast["else"] is List<Dictionary<string, object>> elseExprsList)
                    {
                        foreach (var expr in elseExprsList)
                        {
                            await foreach (var chunk in EvalAst(expr, config, env, runtime))
                            {
                                yield return chunk;
                            }
                        }
                    }
                }
            }
        }
    }
}
