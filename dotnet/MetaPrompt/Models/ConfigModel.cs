using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Models
{
    public class ConfigModel
    {
        public Dictionary<string, string> Parameters { get; }
        public int IfRetries { get; set; } = 3;

        public ConfigModel(Dictionary<string, string> parameters)
        {
            Parameters = parameters;
        }
    }
}
