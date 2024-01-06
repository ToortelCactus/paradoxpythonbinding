import os
from enum import Enum
from helpers import br, eq
from defines import *

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
        folder = MOD_PATH + "events/" + folder

        # create directory if needed
        os.makedirs(folder, exist_ok=True)

        self.filepath = folder + "/" + file
        with open(self.filepath + ".txt", "w") as f:
            f.write("namespace = " + file + "\n\n")

        global currentFile
        currentFile = self

    def export(self, text: str):
        with open(self.filepath + ".txt", "a") as f:
            f.write(text + "\n\n\n")


class DecisionFile(ScriptFile):
    def __init__(self, file: str, folder: str = ""):
        """ file= 'usa_decisions', folder= 'USA_decisions/another_folder'"""
        self.name = file
        folder = MOD_PATH + "common/decisions/" + folder

        # create directory if needed
        os.makedirs(folder, exist_ok=True)

        self.filepath = folder + "/" + file

        global currentFile # TODO: into base class
        currentFile = self

    def export(self, text: str):
        with open(self.filepath + ".txt", "w") as f:
            f.write(text + "\n\n\n")


class ModifierFile(ScriptFile):
    def __init__(self, file: str, folder: str = ""):
        """ file= 'some_modifiers', folder= 'USA/another_folder'"""
        self.name = file
        folder = MOD_PATH + "common/modifiers/" + folder

        # create directory if needed
        os.makedirs(folder, exist_ok=True)

        self.filepath = folder + "/" + file

        global currentFile # TODO: into base class
        currentFile = self

    def export(self, text: str):
        with open(self.filepath + ".txt", "w") as f:
            f.write(text + "\n\n\n")


class HistoryFile(ScriptFile):
    """
    REMOVES EVERYTHING IN ORIGINAL FILE
    TODO: something has to be done about that...
    """
    class Category(Enum):
        characters = 1
        population = 2
        countries = 3
        government = 4

    def __init__(self, category: Category, country: str):
        """ country= 'arg - argentina' (<tag> - <full name>)"""
        folder = MOD_PATH + "common/history/" + category.name
        file = country

        # create directory if needed
        os.makedirs(folder, exist_ok=True)

        self.tag = country[:3]
        self.content = ""
        self.category = category
        self.filepath = folder + "/" + file

        global currentFile
        currentFile = self

        # hack - python shenanigans make "open" disappear in __del__
        self.f = open(self.filepath + ".txt", "w")

    def __del__(self):
        self.f.write(eq(self.category.name.upper(), br(eq("c:" + self.tag, br(self.content)))) + "\n")
        self.f.close()  # the other part of hack

    def export(self, text: str):
        self.content += text + "\n\n"


def getlocalscriptfile() -> ScriptFile:
    global currentFile
    if currentFile is None:
        raise RuntimeError("Forgot to declare scriptfile name first")
    return currentFile
