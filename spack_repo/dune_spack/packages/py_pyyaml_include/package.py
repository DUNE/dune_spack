from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyyamlInclude(PythonPackage):
    """An extending constructor of PyYAML: include other YAML files into YAML document."""

    homepage = "https://github.com/tanbro/pyyaml-include"
    pypi = "pyyaml-include/pyyaml-include-1.4.1.tar.gz"

    # h5flow needs the 1.x API (pyyaml-include<2.0)
    version("1.4.1", sha256="1a96e33a99a3e56235f5221273832464025f02ff3d8539309a3bf00dec624471")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm")

    depends_on("py-pyyaml@6", type=("build", "run"))
