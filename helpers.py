

def br(content: str, layer=0) -> str:
    return "{\n" + content + ("\t"*layer) + "\n}"


def eq(a: str, b: str) -> str:
    return a + " = " + b


def ge(a: str, b: str) -> str:
    return a + " > " + b


def default(function_name: str, assigned_val: str) -> str:
    return eq(function_name, assigned_val)


def iterator(filter: str, effects: str) -> str:
    """{ limit = { <triggers> } <effects> }"""
    return br(eq("limit", br(filter)) + "\n" + effects)


def random_iterator(filter: str, effects: str, mtth: str = ""):
    """{ limit = { <triggers> } (optional) weight = { mtth } <effects> }"""
    if mtth:
        mtth = eq("weight", br(mtth))
    return br(eq("limit", br(filter)) + "\n" + mtth + "\n" + effects)


def effects_to_script(effects: list, layer: int = 1) -> str:
    contents = ""
    for effect in effects:
        contents += ("    " * layer) + effect + "\n"
    return contents


