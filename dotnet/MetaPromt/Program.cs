using Antlr4.Runtime;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Xml;

public class Program
{
    public static Dictionary<string, object> ParseMetaPrompt(string prompt)
    {
        var inputStream = new AntlrInputStream(prompt);
        var lexer = new MetaPromptLexer(inputStream);
        var tokenStream = new CommonTokenStream(lexer);
        var parser = new MetaPromptParser(tokenStream);

        parser.RemoveErrorListeners();
        parser.AddErrorListener(new ThrowingErrorListener());

        var tree = parser.prompt();
        var visitor = new MetaPromptASTBuilder();
        return visitor.VisitPrompt(tree);
    }

    public static async Task Main(string[] args)
    {
        string prompt = @"
        Write me a poem about [:subject]

        [:if [:subject] is a human
           :then
           Use jokingly exaggerated style
        :else
           Include some references to [$ List some people who have any
           relation to [:subject], comma-separated
           ]
        ]";

        var ast = ParseMetaPrompt(prompt);

        var config = new Config(new Dictionary<string, string> { { "subject", "Saint Petersburg" } });

        try
        {
            string result = await EvalMetaPrompt(ast, config);
            Console.WriteLine("Final Result:");
            Console.WriteLine(result);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error during evaluation: {ex.Message}");
        }
    }

    static string LlmInput(string prompt)
    {
        Console.WriteLine($"Prompt to user: {prompt}");
        Console.Write("User Input: ");
        return Console.ReadLine();
    }

    public static async Task<string> EvalMetaPrompt(Dictionary<string, object> metaprompt, Config config)
    {
        Console.WriteLine("Starting EvalMetaPrompt...");
        var env = new Env(config.Parameters);
        var runtime = new Runtime(config, env);
        string result = "";

        await foreach (var chunk in EvalAst(metaprompt, runtime))
        {
            Console.WriteLine($"Chunk evaluated: {chunk}");
            result += chunk;
        }

        Console.WriteLine("EvalMetaPrompt completed.");
        return result;
    }

    public static async IAsyncEnumerable<string> EvalAst(Dictionary<string, object> ast, Runtime runtime)
    {
        Console.WriteLine($"Evaluating AST node of type: {ast["type"]}");

        if (ast["type"].ToString() == "text")
        {
            Console.WriteLine($"Text node: {ast["text"]}");
            yield return ast["text"].ToString();
        }
        else if (ast["type"].ToString() == "metaprompt")
        {
            Console.WriteLine("Processing 'metaprompt' node...");
            if (ast["exprs"] is Dictionary<string, object> exprsDict && exprsDict["exprs"] is List<object> exprsList)
            {
                foreach (var expr in exprsList)
                {
                    if (expr is Dictionary<string, object> exprDict)
                    {
                        await foreach (var chunk in EvalAst(exprDict, runtime))
                        {
                            yield return chunk;
                        }
                    }
                }
            }
        }
        else if (ast["type"].ToString() == "var")
        {
            string value = runtime.Env.Get(ast["name"].ToString());
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

            if (ast["exprs"] is List<object> exprsList)
            {
                foreach (var expr in exprsList)
                {
                    if (expr is Dictionary<string, object> exprDict)
                    {
                        await foreach (var chunk in EvalAst(exprDict, runtime))
                        {
                            chunks.Add(chunk);
                        }
                    }
                }
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

            if (ast["condition"] is Dictionary<string, object> conditionAst &&
                conditionAst.ContainsKey("exprs") &&
                conditionAst["exprs"] is List<object> conditionExprs)
            {
                foreach (var expr in conditionExprs)
                {
                    if (expr is Dictionary<string, object> exprDict)
                    {
                        await foreach (var chunk in EvalAst(exprDict, runtime))
                        {
                            conditionChunks.Add(chunk);
                        }
                    }
                }
            }

            string condition = string.Join("", conditionChunks);
            Console.WriteLine($"Condition evaluated to: {condition}");

            string promptResult = "";
            int retries = 0;
            string prompt = "Please determine if the following statement is true or false:\n" + condition;

            while (promptResult != "true" && promptResult != "false" && retries < runtime.Config.IfRetries)
            {
                promptResult = LlmInput(prompt).Trim();
                Console.WriteLine($"User input for condition check: {promptResult} (Attempt {retries})");
                retries++;
            }

            if (promptResult == "true")
            {
                Console.WriteLine("Executing 'then' block...");
                if (ast["then"] is Dictionary<string, object> thenBlock && thenBlock.TryGetValue("exprs", out var thenExprsObj) && thenExprsObj is List<object> thenExprsList)
                {
                    foreach (var expr in thenExprsList)
                    {
                        if (expr is Dictionary<string, object> exprDict)
                        {
                            await foreach (var chunk in EvalAst(exprDict, runtime))
                            {
                                yield return chunk;
                            }
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
                if (ast["else"] is Dictionary<string, object> elseBlock && elseBlock.TryGetValue("exprs", out var elseExprsObj) && elseExprsObj is List<object> elseExprsList)
                {
                    foreach (var expr in elseExprsList)
                    {
                        if (expr is Dictionary<string, object> exprDict)
                        {
                            await foreach (var chunk in EvalAst(exprDict, runtime))
                            {
                                yield return chunk;
                            }
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

    public static async IAsyncEnumerable<string> EvalExprs(List<Dictionary<string, object>> exprs, Runtime runtime)
    {
        foreach (var expr in exprs)
        {
            await foreach (var chunk in EvalAst(expr, runtime))
            {
                yield return chunk;
            }
        }
    }
}

// Вспомогательные классы
public class Config
{
    public Dictionary<string, string> Parameters { get; }
    public int IfRetries { get; set; } = 3;

    public Config(Dictionary<string, string> parameters)
    {
        Parameters = parameters;
    }
}

public class Env
{
    private readonly Dictionary<string, string> _variables;
    private readonly Env _parent;

    public Env(Dictionary<string, string> variables, Env parent = null)
    {
        _variables = variables;
        _parent = parent;
    }

    public void Set(string variable, string value)
    {
        _variables[variable] = value;
    }

    public string Get(string variable)
    {
        if (_variables.ContainsKey(variable))
            return _variables[variable];
        return _parent?.Get(variable);
    }
}

public class Runtime
{
    public Config Config { get; }
    public Env Env { get; }

    public Runtime(Config config, Env env)
    {
        Config = config;
        Env = env;
    }
}
