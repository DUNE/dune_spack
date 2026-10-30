from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class EdepSim(CMakePackage):
    """edep-sim -- an energy deposit simulation based on Geant4 (DUNE fork)"""

    homepage = "https://github.com/DUNE/edep-sim"
    git = "https://github.com/DUNE/edep-sim.git"

    license("MIT")

    version("4.0.0", tag="4.0.0")
    version("master", branch="master")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.0:", type="build")

    depends_on("root")
    depends_on("geant4@10:")
    depends_on("nlohmann-json")

    def setup_run_environment(self, env):
        env.set("EDEP_ROOT", self.prefix)
        env.set("EDEPSIM_LIB", self.prefix.lib)
        env.set("EDEPSIM_INC", self.prefix.include)
