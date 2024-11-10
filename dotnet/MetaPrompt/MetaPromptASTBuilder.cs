using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MetaPrompt
{
    public class MetaPromptASTBuilder : MetaPromptBaseVisitor<List<Dictionary<string, object>>>
    {
        public override List<Dictionary<string, object>> VisitPrompt(MetaPromptParser.PromptContext context)
        {
            Console.WriteLine("VisitPrompt called.");
            var exprs = VisitExprs(context.exprs()) ?? new List<Dictionary<string, object>>();
            var result = new Dictionary<string, object> { { "type", "metaprompt" }, { "exprs", exprs } };
            Console.WriteLine($"VisitPrompt result: {FormatOutput(new List<Dictionary<string, object>> { result })}");
            return new List<Dictionary<string, object>> { result };
        }

        public override List<Dictionary<string, object>> VisitExprs(MetaPromptParser.ExprsContext context)
        {
            var exprs = new List<Dictionary<string, object>>();
            Console.WriteLine("VisitExprs called.");

            foreach (var expr in context.expr())
            {
                var exprItems = VisitExpr(expr);

                if (exprItems == null || exprItems.Count == 0)
                {
                    Console.WriteLine("Warning: VisitExpr returned an empty result.");
                    continue;
                }

                foreach (var item in exprItems)
                {
                    if (item.ContainsKey("type") && item.ContainsKey("text"))
                    {
                        var type = item["type"];
                        var text = item["text"];
                        Console.WriteLine($"VisitExpr result: [{type}: {text}]");
                    }
                    else if (item.ContainsKey("type"))
                    {
                        var type = item["type"];
                        Console.WriteLine($"VisitExpr result: [{type}]");
                    }
                    else
                    {
                        Console.WriteLine("Warning: Item from VisitExpr is missing 'type' key.");
                    }
                    exprs.Add(item);
                }
            }

            Console.WriteLine($"VisitExprs result: {FormatOutput(exprs)}");
            return exprs;
        }

        public override List<Dictionary<string, object>> VisitExpr(MetaPromptParser.ExprContext context)
        {
            Console.WriteLine("VisitExpr called.");
            var items = new List<Dictionary<string, object>>();

            if (context.text() != null)
            {
                var textResult = VisitText(context.text());
                if (textResult != null && textResult.Count > 0)
                {
                    items.AddRange(textResult);
                }
            }

            if (context.expr1() != null)
            {
                var expr1 = VisitExpr1(context.expr1()) ?? new List<Dictionary<string, object>>();

                if (expr1.Count > 0 && expr1[0].ContainsKey("type"))
                {
                    var type = expr1[0]["type"].ToString();
                    if (type == "meta" || type == "if_then_else" || type == "assign" || type == "var")
                    {
                        items.Add(expr1[0]);
                    }
                    else if (type == "exprs")
                    {
                        // Добавляем скобки как отдельные текстовые узлы
                        items.Add(new Dictionary<string, object> { { "type", "text" }, { "text", "[" } });
                        var exprsContent = expr1[0]["exprs"] as List<Dictionary<string, object>> ?? new List<Dictionary<string, object>>();
                        items.AddRange(exprsContent);
                        items.Add(new Dictionary<string, object> { { "type", "text" }, { "text", "]" } });
                    }
                    else
                    {
                        items.AddRange(expr1);
                    }
                }
                else
                {
                    items.AddRange(expr1);
                }
            }
            else
            {
                // Если expr1 отсутствует, проверяем наличие скобок и выбрасываем исключение
                if (context.RB() != null)
                {
                    throw new Exception("Unexpected ']' without matching '['.");
                }
                if (context.LB() != null)
                {
                    throw new Exception("Unexpected '[' without matching content.");
                }
            }

            Console.WriteLine($"VisitExpr result: {FormatOutput(items)}");
            return items;
        }

        public override List<Dictionary<string, object>> VisitExpr1(MetaPromptParser.Expr1Context context)
        {
            Console.WriteLine("VisitExpr1 called.");
            List<Dictionary<string, object>> result;

            if (context.meta_body() != null)
            {
                result = VisitMeta_body(context.meta_body()) ?? new List<Dictionary<string, object>>();
            }
            else
            {
                result = new List<Dictionary<string, object>>
            {
                new Dictionary<string, object>
                {
                    { "type", "exprs" },
                    { "exprs", VisitExprs(context.exprs()) ?? new List<Dictionary<string, object>>() }
                }
            };
            }

            Console.WriteLine($"VisitExpr1 result: {FormatOutput(result)}");
            return result;
        }

        public override List<Dictionary<string, object>> VisitMeta_body(MetaPromptParser.Meta_bodyContext context)
        {
            Console.WriteLine("VisitMeta_body called.");
            var result = new List<Dictionary<string, object>>();
            var node = new Dictionary<string, object>();

            if (context.ELSE_KW() != null)
            {
                // IF_KW exprs THEN_KW exprs ELSE_KW exprs
                var conditionNode = VisitExprs(context.exprs(0)) ?? new List<Dictionary<string, object>>();
                var thenNode = VisitExprs(context.exprs(1)) ?? new List<Dictionary<string, object>>();
                var elseNode = VisitExprs(context.exprs(2)) ?? new List<Dictionary<string, object>>();
                node = new Dictionary<string, object>
            {
                { "type", "if_then_else" },
                { "condition", conditionNode },
                { "then", thenNode },
                { "else", elseNode }
            };
            }
            else if (context.IF_KW() != null)
            {
                // IF_KW exprs THEN_KW exprs
                var conditionNode = VisitExprs(context.exprs(0)) ?? new List<Dictionary<string, object>>();
                var thenNode = VisitExprs(context.exprs(1)) ?? new List<Dictionary<string, object>>();
                node = new Dictionary<string, object>
            {
                { "type", "if_then_else" },
                { "condition", conditionNode },
                { "then", thenNode },
                { "else", new List<Dictionary<string, object>>() }
            };
            }
            else if (context.VAR_NAME() != null)
            {
                string varName = context.VAR_NAME().GetText().Substring(1); // Удаляем ":" из имени переменной
                if (context.EQ_KW() != null)
                {
                    // [:var_name= value]
                    var exprs = VisitExprs(context.exprs(0)) ?? new List<Dictionary<string, object>>();
                    node = new Dictionary<string, object>
                {
                    { "type", "assign" },
                    { "name", varName },
                    { "exprs", exprs }
                };
                }
                else
                {
                    // [:var_name]
                    node = new Dictionary<string, object>
                {
                    { "type", "var" },
                    { "name", varName }
                };
                }
            }
            else if (context.META_KW() != null)
            {
                // [$ exprs]
                var exprs = VisitExprs(context.exprs(0)) ?? new List<Dictionary<string, object>>();
                node = new Dictionary<string, object>
            {
                { "type", "meta" },
                { "exprs", exprs }
            };
            }
            else
            {
                throw new Exception("Unable to build AST: Unknown meta_body construct.");
            }

            Console.WriteLine($"VisitMeta_body result: {FormatOutput(node)}");
            result.Add(node);
            return result;
        }

        public override List<Dictionary<string, object>> VisitText(MetaPromptParser.TextContext context)
        {
            Console.WriteLine("VisitText called.");
            string text = string.Concat(context.CHAR().Select(c => c.GetText()));
            // Condense multiple spaces into one
            //text = Regex.Replace(text, @"\s+", " ");

            var result = new List<Dictionary<string, object>>
        {
            new Dictionary<string, object> { { "type", "text" }, { "text", text } }
        };
            Console.WriteLine($"VisitText result: {FormatOutput(result)}");
            return result;
        }

        private string FormatOutput(Dictionary<string, object> dict)
        {
            return "{" + string.Join(", ", dict.Select(kv => $"[{kv.Key}: {kv.Value}]")) + "}";
        }

        private string FormatOutput(List<Dictionary<string, object>> list)
        {
            return string.Join(", ", list.Select(dict => FormatOutput(dict)));
        }
    }

}
