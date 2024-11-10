using MetaPrompt.Models;
using MetaPrompt.Services.Bases;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt
{
    public class ConsoleMetaPromptEvaluator : MetaPromptEvaluator
    {
        public ConsoleMetaPromptEvaluator(ConfigModel config) : base(config, new ConsoleLLMService())
        {
        }
    }
}
