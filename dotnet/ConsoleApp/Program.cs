using MetaPrompt;
using MetaPrompt.Models;
using OllamaSharp;

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

var ast = ParseMetaprompt.Parse(prompt);

var config = new ConfigModel(new Dictionary<string, Func<string>>
{
    { "subject", () => "Saint Petersburg" }
});

try
{
    MetaPromptEvaluator metaPromptEvaluator = new OllamaMetaPromptEvaluator(
        new OllamaApiClient(new Uri("http://localhost:11434"), "llama3.1"));

    string result = await metaPromptEvaluator.EvaluateAsync(ast, config);
    Console.WriteLine("\n\nFinal Result:");
    Console.WriteLine(result);
}
catch (Exception ex)
{
    Console.WriteLine($"Error during evaluation: {ex.Message}");
}