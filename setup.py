from distutils.core import setup, Extension
from Cython.Build import cythonize

def get_python_file():
    return input("[ • ] Input file : ")

python_file = get_python_file()

setup(
    name=python_file,
    ext_modules=cythonize(Extension(
        python_file,
        sources=[f"{python_file}", "{python_file}.cpp"],  # Menambahkan ekstensi .py pada nama file
        libraries=[python_file],
        language="c++",
    )),
    script_args=["build_ext"],
    options={"build_ext": {"inplace": True}},
)