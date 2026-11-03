from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPylandau(PythonPackage):
    """A Landau PDF definition to be used in Python."""

    homepage = "https://github.com/SiLab-Bonn/pylandau"
    pypi = "pylandau/pylandau-3.0.0.tar.gz"

    version("3.0.0", sha256="91b0e9e3545d9396e5da8bfe64b953af91585054425b6128ec662df7dcf0f344")
    # 2.x is a Cython extension. 3.x needs numba, whose llvmlite needs llvm@15:16
    # or llvm@20, while dunesw pins llvm@18, so only 2.x fits a dunesw env.
    version("2.2.1", sha256="5dd1cb2c42fda284fd0c69b61abac6238e1379991ce306358131cf59e5623c57")

    depends_on("c", type="build")
    depends_on("cxx", type="build", when="@2")
    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-wheel")
        depends_on("py-cython@0.29:", when="@2")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@3:")
        depends_on("py-numpy@1.21:")
        # setup.py compiles an ahead-of-time numba extension
        depends_on("py-numba@0.53:", when="@3:")
        depends_on("py-scipy@1.7:", when="@3:")
