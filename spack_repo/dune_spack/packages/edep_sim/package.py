from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class EdepSim(CMakePackage):
    """edep-sim -- an energy deposit simulation based on Geant4 (DUNE fork)"""

    homepage = "https://github.com/DUNE/edep-sim"
    git = "https://github.com/DUNE/edep-sim.git"

    license("MIT")

    version("4.0.0", tag="4.0.0")
    version("master", branch="master")

    variant(
        "particlebomb",
        default=False,
        description="Enable the ParticleBomb (MPV/MPR) generator from DLPGenerator",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.0:", type="build")

    # Geant4 as in the sim2x2 container; ROOT as in the dunesw upstream stack
    depends_on("root@6.28.12")
    depends_on("geant4@10.7.4")
    depends_on("nlohmann-json")

    depends_on("yaml-cpp@0.8.0 +shared", when="+particlebomb")
    depends_on("dlpgenerator", when="+particlebomb")

    def cmake_args(self):
        return [self.define_from_variant("EDEPSIM_USE_PARTICLEBOMB", "particlebomb")]

    def setup_build_environment(self, env):
        if self.spec.satisfies("+particlebomb"):
            dlp = self.spec["dlpgenerator"].prefix
            env.set("DLPGENERATOR_INCDIR", dlp.include)
            env.set("DLPGENERATOR_LIBDIR", dlp.lib)

    def setup_run_environment(self, env):
        env.set("EDEP_ROOT", self.prefix)
        env.set("EDEPSIM_LIB", self.prefix.lib)
        env.set("EDEPSIM_INC", self.prefix.include)
