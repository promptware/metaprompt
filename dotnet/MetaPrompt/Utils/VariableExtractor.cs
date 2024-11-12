using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt.Utils
{
    public class VariableExtractor
    {
        public static IEnumerable<Dictionary<string, string>> DiscoverVariables(object ast)
        {
            if (ast is IList astList)
            {
                foreach (var node in astList)
                {
                    foreach (var result in DiscoverVariables(node))
                    {
                        yield return result;
                    }
                }
            }
            else if (ast is IDictionary<string, object> astDict)
            {
                if (astDict.TryGetValue("type", out var typeValue) && typeValue is string type)
                {
                    if (type == "var")
                    {
                        yield return new Dictionary<string, string> { { "type", "var" }, { "name", astDict["name"].ToString() } };
                    }
                    else if (type == "assign")
                    {
                        yield return new Dictionary<string, string> { { "type", "assign" }, { "name", astDict["name"].ToString() } };
                    }
                }

                foreach (var key in astDict.Keys)
                {
                    foreach (var result in DiscoverVariables(astDict[key]))
                    {
                        yield return result;
                    }
                }
            }
        }

        public static HashSet<string> ExtractVariables(object ast)
        {
            var variables = new HashSet<string>();
            var assigned = new HashSet<string>();

            foreach (var item in DiscoverVariables(ast))
            {
                if (item.TryGetValue("type", out var type) && item.TryGetValue("name", out var name))
                {
                    switch (type)
                    {
                        case "var" when !assigned.Contains(name):
                            variables.Add(name);
                            break;
                        case "assign":
                            assigned.Add(name);
                            break;
                    }
                }
            }

            return variables;
        }
    }
}