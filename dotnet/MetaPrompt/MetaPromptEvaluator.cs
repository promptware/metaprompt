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

            Console.WriteLine($"Evaluating AST node of type: {ast["type"]}");

            if (ast["type"].ToString() == "text")
            {
                Console.WriteLine($"Text node: {ast["text"]}");
                yield return ast["text"].ToString();
            }
            else if (ast["type"].ToString() == "metaprompt")
            {
                Console.WriteLine("Processing 'metaprompt' node...");
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
                else
                {
                    Console.WriteLine("Error: 'exprs' is not a list of expressions.");
                }
            }
            else if (ast["type"].ToString() == "exprs")
            {
                Console.WriteLine("Processing 'exprs' node...");
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
                else
                {
                    Console.WriteLine("Error: 'exprs' is not a list of expressions.");
                }
            }
            else if (ast["type"].ToString() == "var")
            {
                string value = _runtime.Env.Get(ast["name"].ToString());
                Console.WriteLine($"Variable '{ast["name"]}' resolved to: {value}");
                if (value == null)
                {
                    throw new Exception($"Variable not found: {ast["name"]}");
                }
                yield return value;
            }
            else if (ast["type"].ToString() == "meta")
            {
                Console.WriteLine("Processing 'meta' node...");
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
                else
                {
                    Console.WriteLine("Error: 'exprs' is not a list of expressions.");
                }

                string metaPrompt = string.Join("", chunks);
                Console.WriteLine($"Meta-prompt generated: {metaPrompt}");
                string output = LlmInput(metaPrompt);
                yield return output;
            }
            else if (ast["type"].ToString() == "if_then_else")
            {
                Console.WriteLine("Processing 'if_then_else' node...");
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
                Console.WriteLine($"Condition evaluated to: {condition}");

                string promptResult = "";
                int retries = 0;
                string prompt = "Please determine if the following statement is true or false:\n" + condition;

                while (promptResult != "true" && promptResult != "false" && retries < _runtime.Config.IfRetries)
                {
                    promptResult = LlmInput(prompt).Trim();
                    Console.WriteLine($"User input for condition check: {promptResult} (Attempt {retries})");
                    retries++;
                }

                if (promptResult == "true")
                {
                    Console.WriteLine("Executing 'then' block...");
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
                    else
                    {
                        Console.WriteLine("Error: 'then' block is missing or has an incorrect format.");
                    }
                }
                else
                {
                    Console.WriteLine("Executing 'else' block...");
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
                    else
                    {
                        Console.WriteLine("Error: 'else' block is missing or has an incorrect format.");
                    }
                }
            }
            else
            {
                Console.WriteLine($"Unknown node type: {ast["type"]}");
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
