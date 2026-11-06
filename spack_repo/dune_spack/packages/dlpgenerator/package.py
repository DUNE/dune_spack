from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *


class Dlpgenerator(MakefilePackage):
    """DLPGenerator -- the ParticleBomb (MPV/MPR) particle generator library
    (libLiteFMWK_ParticleBomb) used by edep-sim."""

    homepage = "https://github.com/DeepLearnPhysics/DLPGenerator"
    git = "https://github.com/DeepLearnPhysics/DLPGenerator.git"

    version("1.4.0", tag="v1.4.0", preferred=True)
    # The sim2x2 container's commit. It has no release tag, so the label is the
    # short hash and `commit=` pins the source.
    version("1af8cbf", commit="1af8cbfa13db5478542a3da9e9b61c57fa617d38")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("root@6.28.12")

    # The per-package makefiles create directories as they go
    parallel = False

    def setup_build_environment(self, env):
        src = self.stage.source_path
        build = join_path(src, "build")
        env.set("DLPGENERATOR_DIR", src)
        env.set("DLPGENERATOR_BUILDDIR", build)
        env.set("DLPGENERATOR_LIBDIR", join_path(build, "lib"))
        env.set("DLPGENERATOR_INCDIR", join_path(build, "include"))
        env.set("DLPGENERATOR_CXX", "g++")
        # setup.sh would probe for numpy; ParticleBomb does not need it
        env.set("DLPGENERATOR_NUMPY", "0")
        env.set("DLPGENERATOR_ROOT6", "1")

    def install(self, spec, prefix):
        install_tree(join_path("build", "lib"), prefix.lib)
        install_tree(join_path("build", "include"), prefix.include)
        # ROOT looks for the dictionary module next to the library
        for pcm in find("build", "*_rdict.pcm"):
            install(pcm, prefix.lib)

    def setup_run_environment(self, env):
        env.set("DLPGENERATOR_INCDIR", self.prefix.include)
        env.set("DLPGENERATOR_LIBDIR", self.prefix.lib)
