
from cx_Freeze import setup, Executable
import sys, os

os.environ['TCL_LIBRARY'] = 'C:/Users/TomekP/AppData/Local/Programs/Python/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/TomekP/AppData/Local/Programs/Python/Python36-32/tcl/tk8.6'

base = None

if sys.platform == 'win32':
    base = "Win32GUI"


executables = [Executable("gui.py", base=base)]

packages = ['idna']
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "GeneratorUmow",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables
)
