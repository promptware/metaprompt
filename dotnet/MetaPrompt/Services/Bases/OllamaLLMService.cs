using Microsoft.Extensions.AI;
using OllamaSharp;
using OllamaSharp.MicrosoftAi;
using OllamaSharp.Models;
using System.Text.Json;
using System.Text;
using System.Threading.Tasks;
using MetaPrompt.Services.Interfaces;

public class OllamaLLMService : ILLMService
{
    private readonly OllamaApiClient _ollama;

    public OllamaLLMService(OllamaApiClient ollama)
    {
        _ollama = ollama;
    }

    public async Task<string> GetResponseAsync(string systemPrompt, string prompt, float temperature)
    {
        Console.WriteLine("Prompt: " + systemPrompt + prompt);

        var options = new ChatOptions
        {
            Temperature = temperature  // Установка температуры
        };

        var request = AbstractionMapper.ToOllamaSharpChatRequest(new List<ChatMessage>
        {
            new ChatMessage
            {
                Role = ChatRole.System,
                Text = systemPrompt
            },
            new ChatMessage
            {
                Role = ChatRole.User,
                Text = prompt
            }
        }, options, stream: true, JsonSerializerOptions.Default);

        // Отправляем запрос и обрабатываем ответ
        var response = new StringBuilder();
        await foreach (var result in _ollama.ChatAsync(request))
        {
            if (result != null)
            {
                response.Append(result.Message?.Content);
            }
        }

        Console.WriteLine("FullResponse: " + response);

        return response.ToString();
    }
}
