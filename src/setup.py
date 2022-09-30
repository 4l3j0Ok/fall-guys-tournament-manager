import sys
import os
import config
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Fall Guys To",
    version = config.APP_VERSION,
    description = "Tus torneos, tus reglas.",
    author = "Alejoide",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
