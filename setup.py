from cx_Freeze import setup, Executable

config = Executable(
    script='main.py'
)

setup(
    name='Faker generate',
    version='1.0',
    description='This program generates a JSON file with data from Faker.',
    author='Alexsander Sauter',
    executables=[config]
)