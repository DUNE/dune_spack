from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyH5flow(PythonPackage):
    """A workflow framework centered around hdf5 file access."""

    homepage = "https://github.com/DUNE/h5flow"
    url = "https://github.com/DUNE/h5flow/archive/refs/tags/v0.2.5.tar.gz"
    git = "https://github.com/DUNE/h5flow.git"

    version("main", branch="main")
    # The v0.2.5 tag's VERSION file still says 0.2.4
    version("0.2.5", sha256="d8d4fba2882f0396da6a2c8dfc8d3a098130e0d2996eb54af822abe0083383cd")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.7:")
        depends_on("py-numpy")
        depends_on("py-h5py@2.10:")
        depends_on("py-pyyaml")
        depends_on("py-pyyaml-include@:1")
        depends_on("py-tqdm")
        depends_on("py-pytest")
