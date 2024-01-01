from typing import List


def tab_contents(contents: str):
    """ tab contents separated by newlines """
    result = ""
    for line in contents.splitlines(keepends=True):
        result += "    " + line
    return result


def add_if_defined(name: str, content):
    if content:
        return eq(name, content) + "\n"
    return ""


def br(content: str, layer=0) -> str:
    return "{\n" + tab_contents(content) + "\n}"


def eq(a: str, b: str) -> str:
    return a + " = " + b + " "


def eqn(a: str, b: str) -> str:
    return a + " = " + b + "\n"


def ge(a: str, b: str) -> str:
    return a + " > " + b + " "


def default(function_name: str, assigned_val: str) -> str:
    return eq(function_name, assigned_val)


def default_list(function_name: str, assigned_list: List[str]) -> str:
    return eq(function_name, list_to_text(assigned_list))


def iterator(filter: str, effects: str) -> str:
    """{ limit = { <triggers> } <effects> }"""
    return br(eq("limit", br(filter)) + "\n" + effects)


def random_iterator(filter: str, effects: str, mtth: str = ""):
    """{ limit = { <triggers> } (optional) weight = { mtth } <effects> }"""
    if mtth:
        mtth = eq("weight", br(mtth))
    return br(eq("limit", br(filter)) + "\n" + mtth + "\n" + effects)


def list_to_text(effects: list) -> str:
    contents = ""
    for effect in effects:
        contents += effect + "\n"
    return contents


