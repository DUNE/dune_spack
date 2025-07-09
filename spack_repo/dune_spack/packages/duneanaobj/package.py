# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install duneanaobj
#
# You can edit this file again by typing:
#
#     spack edit duneanaobj
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Duneanaobj(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/duneanaobj/archive/refs/tags/v03_10_00.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("03_10_00", sha256="35f025b77b3f5c6cc4666d1bbd04b2ff8f837a51670bbe5c0d80a7e3145164d8")
    version("03_06_01", sha256="ad0647930712d5680c77c03f8d0af3a9e44f222c15c753d631ac8752ddf07e67")
    version("03_06_00", sha256="28be5276666146e88501fe73df6907fde9552969824e8f7dc8115598c914d5da")
    version("03_05_00", sha256="00e227bccf02ef0c8faa5931b39b6f6c65ff88563e2c328e35e1c3109bcf8c63")
    version("03_04_00", sha256="3cfc96a0aae4fab7e51f501b071d9b9bfe32cfaa9bd288a3a9b159fde18b4f3b")
    version("03_03_00", sha256="4d00eaa72997b8ff6a6f59e9eedadd11806ab06c83d28064d523dfa9f00e15e5")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v03_06_01.patch', when="@03_06_01")
    patch('v09_81_00d00.patch', when="@03_03_00")
    # FIXME: Add dependencies if required.
    depends_on("root")
    depends_on("canvas-root-io")
    depends_on("py-srproxy@00.43:", when="@03_03_00")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")
    depends_on("py-srproxy")
    
    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ] 
        return args

    def setup_build_environment(self, spack_env):
        spack_env.set("LD_LIBRARY_PATH", "%s/root" % self.spec["root"].prefix.lib)
        spack_env.set("ROOT_INC", "%s" % self.spec["root"].prefix.include)
        spack_env.set("DUNEANAOBJ_DIR", "%s" % self.stage.source_path)
        spack_env.set("MRB_BUILDDIR", "%s" % self.build_directory)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        run_env.append_path("FHICL_FILE_PATH", "{0}/fcl".format(self.prefix))
        run_env.append_path("FW_SEARCH_PATH", "{0}/gdml".format(self.prefix))

    def setup_dependent_run_environment(self, run_env, dspec):
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        run_env.append_path("FHICL_FILE_PATH", "{0}/fcl".format(self.prefix))
        run_env.append_path("FW_SEARCH_PATH", "{0}/gdml".format(self.prefix))
