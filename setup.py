import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python37\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Medivision Software",
    options = {"build_exe": {"packages":["tkinter","PyQt5","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll','MenuBar','src','ToolBar','Masters.py','Owner_login.py','toolmenu.py']}},
    version = "8.3",
    description = "Medical Application | Developed By SHUBHAM LOHAR",
    executables = executables
    )
