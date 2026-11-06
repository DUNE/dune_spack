from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDbscan1d(PythonPackage):
    """An efficient implementation of the DBSCAN algorithm for 1D arrays."""

    homepage = "https://github.com/d-chambers/dbscan1d"
    pypi = "dbscan1d/dbscan1d-0.2.3.tar.gz"

    version("0.2.3", sha256="90877622e9f69db93c74a6b92e96f509f472f5811c7281b98513805016f0c1be")

    with default_args(type="build"):
        depends_on("py-setuptools@41:")
        depends_on("py-setuptools-scm")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy@1.25:")
