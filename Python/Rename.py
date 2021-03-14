from pathlib import Path

"""Rename any files inside basePath directory that have nameKey in its file name"""

"""add path to directory"""
basePath = ""

"""make list of any files and directories inside the basePath"""
entries = Path(basePath)

"""key to differenciate between another files if there any"""
nameKey = ""

"""
iterate every files and directories inside the basePath and 
rename any files or directories that matches the rule/s
"""
for entry in entries.iterdir():
    """
    use is_dir() to iterate just directories or just comment this line
    if you want to iterate any files and directories inside basePath
    """
    if entry.is_file():
        if nameKey in entry.name:
            """replace specific string"""
            nameAfter = entry.name.replace("what to replace", "replace with this")
            #nameAfter = "or just straight text here"

            """rename the file"""
            entry.rename(nameAfter)
