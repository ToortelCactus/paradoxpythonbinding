Python alternative to Victoria 3 modding

For hybrid development - some files created using this tool, others using the old paradox scripting way.

IN DEVELOPMENT!
Currently only events, decisions, characters, modifiers, effects, and some triggers are supported. Some validation, scopes and parsing of existing data.

Usage:
- in transferendum_in_pythonis/defines.py change the MOD_PATH to your actual mod path
- open main.py and write events there or just use this code as a library in your own python scripts
- run your script or main.py, files will be generated (!by overwriting, dont use on files you want to preserve!)

Adding enums of existing objects:
- go to "parser" folder and run transferendum_in_pythonis/parser.py, it will recreate generated enum files
