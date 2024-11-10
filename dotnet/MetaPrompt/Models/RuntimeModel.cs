using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Models
{
    public class RuntimeModel
    {
        public ConfigModel Config { get; }
        public EnvModel Env { get; }

        public RuntimeModel(ConfigModel config, EnvModel env)
        {
            Config = config;
            Env = env;
        }
    }
}
