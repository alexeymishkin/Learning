from cx_Freeze import setup, Executable

setup(
    name = "Pars",
    version = "0.2",
    description = "Pars",
    executables = [Executable("PosParser.py")]
)