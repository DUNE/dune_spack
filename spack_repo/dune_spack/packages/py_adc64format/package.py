from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAdc64format(PythonPackage):
    """A python library to parse ADC64-formatted files."""

    homepage = "https://github.com/larpix/adc64format"
    url = "https://github.com/larpix/adc64format/archive/refs/tags/v0.1.5.tar.gz"
    git = "https://github.com/larpix/adc64format.git"

    license("MIT")

    version("0.1.5", sha256="5de1ba330bb3cab1e861aafda73e676941d65b68831d3896b9341b86a2b372e8")

    depends_on("py-setuptools@61:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.8:")
        depends_on("py-numpy")
        depends_on("py-h5py")
        depends_on("py-tqdm")
