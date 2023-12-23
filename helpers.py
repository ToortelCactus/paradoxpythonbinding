

def br(content: str, layer=0) -> str:
    return "{\n" + content + ("\t"*layer) + "\n}"


def eq(a: str, b: str) -> str:
    return a + " = " + b


def default(function_name: str, assigned_val: str) -> str:
    return eq(function_name, assigned_val)


def iterator(filter: str, effects: str) -> str:
    """limit = { <triggers> } <effects>"""
    return eq("limit", br(filter)) + "\n" + effects
