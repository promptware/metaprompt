using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Services.Interfaces
{
    public interface ILLMService
    {
        Task<string> GetResponseAsync(string systemPromt, string prompt, float temperature = 0.5f);
    }
}
