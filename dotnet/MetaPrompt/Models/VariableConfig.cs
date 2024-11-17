using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Models
{
    public class VariableConfig
    {
        private string _cache;
        private readonly Func<VariableParameterContext, string> _resolver;

        public bool IsCache { get; set; }

        public VariableConfig(Func<VariableParameterContext, string> resolver, bool isCache = false)
        {
            _resolver = resolver;
            IsCache = isCache;
        }

        public string Invoke(VariableParameterContext variableParameter)
        {
            if (!string.IsNullOrWhiteSpace(_cache))
                return _cache;

            if (IsCache)
                return _cache = _resolver.Invoke(variableParameter);

            return _resolver.Invoke(variableParameter);
        }
    }

}
