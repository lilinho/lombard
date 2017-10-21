
from cx_Freeze import setup, Executable
import sys, os

os.environ['TCL_LIBRARY'] = 'C:/Users/TomekP/AppData/Local/Programs/Python/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/TomekP/AppData/Local/Programs/Python/Python36-32/tcl/tk8.6'

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [Executable("gui.py", base=base)]

includes      = []
include_files = ["C:/Users/TomekP/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll", \
                 "C:/Users/TomekP/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll", \
				 ("files/umowy.xml", "umowy.xml"), \
				 ("files/umowa_wzor.rtf", "umowa_wzor.rtf"), \
				 ("files/Pomoc.rtf", "Pomoc.rtf")]

target = Executable(
    script="gui.py",
    base=base,
    icon="icon.ico",
	targetName="GeneratorUmow.exe"
    )
setup(
    name = "Test",
    version = "1.0",
    options = {"build_exe": {"includes": includes, "include_files": include_files}},
    executables = [target]
)