import argparse
import os

class ParseSetAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        var_dict = getattr(namespace, self.dest, {})
        if var_dict is None:
            var_dict = {}
        # Split on the first '=' to handle cases where values may contain '='
        name, value = values.split("=", 1)
        var_dict[name] = value
        setattr(namespace, self.dest, var_dict)

def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="MetaPrompt is a template engine for LLM prompts that supports writing prompts with prompts. Visit https://metaprompt-lang.org/ for more info.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Adding positional arguments
    parser.add_argument(
        "INPUT_FILES",
        nargs="*",
        help="A list of metaprompt files."
    )

    parser.add_argument(
        "--set",
        action=ParseSetAction,
        dest="variables",
        metavar="VAR_NAME=value",
        help="define a variable in the form VAR_NAME=value.",
    )

    # Parsing arguments
    return parser.parse_args()

def main():
    args = parse_arguments()
    print(args)
    for file_path in args.INPUT_FILES:
        if os.path.isfile(file_path):
            with open(file_path, 'utf-8') as file:
                content = file.read()
                ast = parse_metaprompt(content)

if __name__ == "__main__":
    main()
