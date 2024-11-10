using MetaPrompt.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt
{
    public class MetaPromptEvaluator
    {
        private readonly ConfigModel _config;
        private readonly EnvModel _env;
        private readonly RuntimeModel _runtime;

        public MetaPromptEvaluator(ConfigModel config)
        {
            _config = config;
            _env = new EnvModel(config.Parameters);
            _runtime = new RuntimeModel(config, _env);
        }

        public async Task<string> EvaluateAsync(Dictionary<string, object> metaprompt)
        {
            string result = "";
            await foreach (var chunk in EvalAst(metaprompt))
            {
                result += chunk;
            }
            return result;
        }

        private async IAsyncEnumerable<string> EvalAst(Dictionary<string, object> ast)
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
                        await foreach (var chunk in EvalAst(expr))
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
                        await foreach (var chunk in EvalAst(expr))
                        {
                            yield return chunk;
                        }
                    }
                }
            }
            else if (ast["type"].ToString() == "var")
            {
                string value = _runtime.Env.Get(ast["name"].ToString());
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
                        await foreach (var chunk in EvalAst(expr))
                        {
                            chunks.Add(chunk);
                        }
                    }
                }

                string metaPrompt = string.Join("", chunks);
                string output = LlmInput(metaPrompt);
                yield return output;
            }
            else if (ast["type"].ToString() == "if_then_else")
            {
                List<string> conditionChunks = new List<string>();

                if (ast["condition"] is List<Dictionary<string, object>> conditionExprs)
                {
                    foreach (var expr in conditionExprs)
                    {
                        await foreach (var chunk in EvalAst(expr))
                        {
                            conditionChunks.Add(chunk);
                        }
                    }
                }

                string condition = string.Join("", conditionChunks);

                string promptResult = "";
                int retries = 0;
                string prompt = "Please determine if the following statement is true or false:\n" + condition;

                while (promptResult != "true" && promptResult != "false" && retries < _runtime.Config.IfRetries)
                {
                    promptResult = LlmInput(prompt).Trim();
                    retries++;
                }

                if (promptResult == "true")
                {
                    if (ast["then"] is List<Dictionary<string, object>> thenExprsList)
                    {
                        foreach (var expr in thenExprsList)
                        {
                            await foreach (var chunk in EvalAst(expr))
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
                            await foreach (var chunk in EvalAst(expr))
                            {
                                yield return chunk;
                            }
                        }
                    }
                }
            }
        }

        string LlmInput(string prompt)
        {
            Console.WriteLine($"Prompt to user: {prompt}");
            Console.Write("User Input: ");
            return Console.ReadLine();
        }
    }
}
