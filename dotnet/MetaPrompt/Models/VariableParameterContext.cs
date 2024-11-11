using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.NetworkInformation;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Models
{
    public class VariableParameterContext
    {
        public string VariableName { get; set; }
        public EnvModel Env { get; set; }
        public Dictionary<string, object> AntParrent { get; set; }
    }
}
