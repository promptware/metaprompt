from ffi import foreign_function, eager, lazy
import os
import requests
import html2text

# Logic


def booleanify(string):
    string = string.strip()
    if string in ["false", "true"]:
        return string == "true"
    else:
        raise ValueError(string + " is not a boolean")


@foreign_function(eager)
def xor(*args, **kwargs):
    res = False
    for arg in args:
        res = not res if booleanify(arg) else res
    for _, arg in kwargs.items():
        res = not res if booleanify(arg) else res
    return "true" if res else "false"


@foreign_function(lazy)
async def _or(*args, **kwargs):
    for arg in args:
        arg = await arg.compute()
        if booleanify(arg):
            return "true"

    for _, arg in kwargs.items():
        arg = await arg.compute()
        if booleanify(arg):
            return "true"

    return "false"


@foreign_function(lazy)
async def _and(*args, **kwargs):
    for arg in args:
        arg = await arg.compute()
        if not booleanify(arg):
            return "false"

    for _, arg in kwargs.items():
        arg = await arg.compute()
        if not booleanify(arg):
            return "false"

    return "true"


# Strings


@foreign_function(eager)
async def cite(string, prefix="> "):
    return "\n".join([prefix + line for line in string.split("\n")])


@foreign_function(eager)
def strip(string):
    return string.strip()


@foreign_function(eager)
def length(string):
    return str(len(string))


# TODO: strip lines
# TODO: replace
# TODO: strip suffix/prefix
# TODO: find

# Web


@foreign_function(eager)
async def google(query):

    GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
    GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_SEARCH_API_KEY,
        "cx": GOOGLE_SEARCH_ENGINE_ID,
        "q": query,
    }

    response = requests.get(url, params=params)

    res = ""

    if response.status_code == 200:
        results = response.json()

        i = 1
        for item in results.get("items", []):
            res += f"[result #{str(i)}]\n"
            res += f"Title: {item['title']}\n"
            res += f"URL: {item['link']}\n"
            res += f"Summary: {item['snippet']}\n"
            i += 1
    else:
        raise ValueError(f"@google: {response.status_code} error")

    return res


@foreign_function(eager)
def read_web(url):
    """
    Downloads a webpage's HTML content and converts it to Markdown.

    Parameters:
        url (str): The URL of the webpage to download.

    Returns:
        str: The Markdown representation of the webpage.
    """
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Convert HTML to Markdown
        html_content = response.text
        markdown_converter = html2text.HTML2Text()
        markdown_converter.ignore_links = True  # Keep links in the Markdown
        markdown_converter.skip_internal_links = (
            True  # Skip internal anchors (optional)
        )
        markdown_converter.ignore_images = True  # Remove image links
        markdown_content = markdown_converter.handle(html_content)

        return markdown_content
    except requests.exceptions.RequestException as e:
        raise ValueError(
            f"@read_web: An error occurred while fetching the URL: {e}"
        )
        return None


prelude = {
    "and": _and,
    "or": _or,
    "xor": xor,
    "cite": cite,
    "strip": strip,
    "google": google,
    "length": length,
    "read_web": read_web,
}
