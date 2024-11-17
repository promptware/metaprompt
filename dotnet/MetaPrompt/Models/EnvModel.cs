using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.NetworkInformation;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Models
{
    public class EnvModel
    {
        private readonly Dictionary<string, VariableConfig> _variables;
        private readonly EnvModel _parent;

        public EnvModel(Dictionary<string, VariableConfig> variables, EnvModel parent = null)
        {
            _variables = variables;
            _parent = parent;
        }

        public void Set(string variable, VariableConfig value)
        {
            _variables[variable] = value;
        }

        public string Get(string variable, Dictionary<string, object> astParrent)
        {
            if (_variables.ContainsKey(variable))
                return _variables[variable].Invoke(new VariableParameterContext() {
                    Env = this,
                    VariableName = variable,
                    AntParrent = astParrent 
                });

            return _parent?.Get(variable, astParrent);
        }
    }
}
