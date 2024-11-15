import asyncio
import argparse
from parse_metaprompt import parse_metaprompt
from env import Env
from runtime import Runtime
import os
from config_loader import load_config
from eval import eval_ast


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
        description="MetaPrompt is a template engine for LLM prompts that supports writing prompts with prompts. Visit https://metaprompt-lang.org/ for more info. Configure API keys via environment variables (.env respected): OPENAI_API_KEY",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Adding positional arguments
    parser.add_argument(
        "INPUT_FILES", nargs="*", help="A list of metaprompt files."
    )

    parser.add_argument(
        "--model",
        type=str,
        help="LLM id to use",
        default="interactive",  # TODO: use dynamic model selection
    )

    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available LLMs for use with --model, based on the available LLM providers",
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


def print_models(config):
    print("Available models:")
    print()
    print("\n".join(["- " + key for key in sorted(config.providers)]))
    print()
    print("Use --model to specify the default model.")


async def _main():
    args = parse_arguments()
    config = load_config()

    if args.list_models:
        print_models(config)
        return

    config.parameters = dict(args.variables or {})
    for file_path in args.INPUT_FILES:
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                metaprompt = parse_metaprompt(content)
                env = Env(env=config.parameters)
                config.model = args.model or "interactive"
                runtime = Runtime(config, env)
                runtime.cwd = os.path.dirname(file_path)
                async for chunk in eval_ast(metaprompt, runtime):
                    print(chunk, end="")


def main():
    asyncio.run(_main())


if __name__ == "__main__":
    main()
