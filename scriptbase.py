import os
from enum import Enum
from helpers import br, eq

global currentFile
currentFile = None
# types?


class ScriptFile:
    def export(self, text: str):
        assert False  # Must be overriden!


class EventFile(ScriptFile):
    def __init__(self, file: str, folder: str = ""):
        """ file= 'usa_events', folder= 'USA_events/another_folder'"""
        self.name = file

        # create directory if needed
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass

        self.filepath = folder + "/" + file
        with open(self.filepath + ".txt", "w") as f: # TODO: yeet out of base class
            f.write("namespace = " + file + "\n\n")

        global currentFile
        currentFile = self

    def export(self, text: str):
        with open(self.filepath + ".txt", "a") as f:
            f.write(text + "\n\n\n")


class HistoryFile(ScriptFile):
    class Category(Enum):
        characters = 1
        population = 2
        countries = 3
        government = 4

    def __init__(self, category: Category, country: str):
        """ country= 'arg - argentina' (<tag> - <full name>)"""
        folder = "common/history/" + category.name
        file = country

        self.tag = country[:3]
        self.content = ""
        self.category = category
        self.filepath = folder + "/" + file

        global currentFile
        currentFile = self

    def __del__(self):
        with open(self.filepath + ".txt", "w") as f:
            f.write(eq(self.category.name.upper(), br(eq("c:" + self.tag, self.content))) + "\n")

    def export(self, text: str):
        self.content += text + "\n\n"


def getlocalscriptfile() -> ScriptFile:
    global currentFile
    if currentFile is None:
        raise RuntimeError("Forgot to declare scriptfile name first")
    return currentFile
