using MetaPrompt;
using MetaPrompt.Models;

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

var config = new ConfigModel(new Dictionary<string, string> { { "subject", "Saint Petersburg" } });

try
{
    MetaPromptEvaluator metaPromptEvaluator = new MetaPromptEvaluator(config);
    string result = await metaPromptEvaluator.EvaluateAsync(ast);
    Console.WriteLine("Final Result:");
    Console.WriteLine(result);
}
catch (Exception ex)
{
    Console.WriteLine($"Error during evaluation: {ex.Message}");
}