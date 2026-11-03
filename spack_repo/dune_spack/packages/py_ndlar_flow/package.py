from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNdlarFlow(PythonPackage):
    """An h5flow-based analysis framework for DUNE ND-LAr simulation and data."""

    homepage = "https://github.com/DUNE/ndlar_flow"
    url = "https://github.com/DUNE/ndlar_flow/archive/refs/tags/v1.6.0.tar.gz"
    git = "https://github.com/DUNE/ndlar_flow.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("1.6.0", sha256="bfbe8124842cf5cb261097bfa224772c452838277bee3917ac10de4d4b80ec35")

    # [build-system] requires
    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-wheel")

    # [project] dependencies. pip runs with --no-deps under Spack, so the
    # "name @ git+https://..." entries are satisfied by the Spack packages below.
    with default_args(type=("build", "run")):
        depends_on("python@3.7:")
        depends_on("py-numpy")
        depends_on("py-h5py@2.10:")
        depends_on("py-pytest")
        depends_on("py-scipy")
        depends_on("py-scikit-image")
        depends_on("py-scikit-learn@1.3.0:")
        depends_on("py-dbscan1d@0.2.3")
        depends_on("py-h5flow")
        depends_on("py-pylandau")
        depends_on("py-adc64format@0.1.5")
        # Imported by src/ but missing from pyproject.toml
        depends_on("py-pyyaml")
        depends_on("py-tqdm")
