global currentFile
currentFile = None
# types?


class ScriptFile:
    def __init__(self, file: str, folder: str = ""):
        """ file= 'usa_events', folder= 'USA_events/another_folder'"""
        self.name = file
        self.filepath = folder + "/" + file
        with open(self.filepath + ".txt", "w") as f:
            f.write("namespace = " + file + "\n\n")

        global currentFile
        currentFile = self

    def export(self, text: str):
        with open(self.filepath + ".txt", "a") as f:
            f.write(text + "\n\n\n")


def getlocalscriptfile() -> ScriptFile:
    global currentFile
    if currentFile is None:
        raise RuntimeError("Forgot to declare scriptfile name first")
    return currentFile
