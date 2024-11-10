using MetaPrompt.Services.Interfaces;
using OllamaSharp;
using OllamaSharp.Models;
using System;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Services.Bases
{
    public class OllamaLLMService : ILLMService
    {
        private readonly OllamaApiClient _ollama;

        public OllamaLLMService(OllamaApiClient ollama)
        {
            _ollama = ollama;
        }

        public async Task<string> GetResponseAsync(string prompt)
        {
            Console.WriteLine("Promt: " + prompt);
            var generateRequest = new GenerateRequest { Prompt = prompt };
            var fullResponse = new StringBuilder();

            try
            {
                await foreach (var response in _ollama.GenerateAsync(generateRequest))
                {
                    if (response != null)
                    {
                        // Use the correct field for response content
                        fullResponse.Append(response.Response);
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error generating response: {ex.Message}");
            }

            Console.WriteLine("FullResponse: " + fullResponse);
            return fullResponse.ToString();
        }
    }
}
