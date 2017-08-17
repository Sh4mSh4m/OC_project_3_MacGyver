import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pandas, pygame, random"]}

base = None


executables = [Executable("macgyver_p3.py", base=base)]


setup(
    name = "macgyver_p3",
    options = {"build.exe": build_exe_options},
    version = "1.0.0.0",
    description = 'MacGyver',
    executables = executables
)