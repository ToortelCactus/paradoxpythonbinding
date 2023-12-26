global currentFile
currentFile = None
# types?


class ScriptFile:
    def __init__(self, file: str):
        self.name = file
        with open(file + ".txt", "w") as f:
            f.write("namespace = " + file + "\n")

        global currentFile
        currentFile = self

    def export(self, text: str):
        with open(self.name + ".txt", "a") as f:
            f.write(text)


def getlocalscriptfile() -> ScriptFile:
    global currentFile
    if currentFile is None:
        raise RuntimeError("Forgot to declare scriptfile name first")
    return currentFile
