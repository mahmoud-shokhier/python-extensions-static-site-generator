import sys, importlib
from pathlib import Path

from numpy import load

def load_module(directory, name):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)
    
def load_directory(directory):
    for path in directory:
        load_module(directory.as_posix(), path.stem)

def load_bundled():
    directory = Path(__file__).parent / "extensions"
    load_directory(directory)


