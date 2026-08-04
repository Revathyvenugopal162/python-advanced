# pep 810
# reduce the startup time of python by lazy importing modules
lazy import json
lazy from pathlib import Path

print("Starting up...")  # json and pathlib not loaded yet

data = json.loads('{"key": "value"}')  # json loads here
p = Path(".")  # pathlib loads here


#a module can define __lazy_modules__ as a container of fully qualified module name strings
__lazy_modules__ = ["json", "pathlib"]

import json     # lazy
import os       # still eager