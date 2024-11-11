using MetaPrompt.Services.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Services.Bases
{
    internal class ConsoleLLMService : ILLMService
    {
        public Task<string> GetResponseAsync(string system, string prompt, float temperature)
        {
            Console.WriteLine($"Prompt to LLM: {system} {prompt}");
            Console.Write("LLM Response: ");
            string response = Console.ReadLine();
            return Task.FromResult(response);
        }
    }
}
