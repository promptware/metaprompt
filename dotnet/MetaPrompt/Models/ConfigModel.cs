using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Models
{
    public class ConfigModel
    {
        public EnvModel Env { get; private set; }
        public int IfRetries { get; set; } = 3;

        public ConfigModel(Dictionary<string, VariableConfig> parameters)
        {
            Env = new EnvModel(parameters);
        }
    }
}
