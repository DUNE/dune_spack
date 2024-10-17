# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.fnal_art.fnal_github_package import *

class Dunesw(CMakePackage, FnalGithubPackage):
    """Dunesw"""

    repo = "DUNE/dunesw"
    version_patterns = ["09_00_00d00", "09.14.19"]

    version("09_92_00d00", sha256="0e3bae89b9e01f3b29303d5b65a72c5122c906e7f54c92ed9f282e13641d12c0")
    version("09_89_01d01", sha256="d516d3f7c00ed99fe23de77152bad556b5a6a24e777e3e5ec7d7a4beddaff3cb")
    version("09_81_00d01", sha256="126477cb91b6fd7a69ef2753505ca8dcd5739f4f509409cbf6f93f0774574862")
    version("09_81_00d00", sha256="f32da1e3e3ac4482674dcd3559c23a8acd10bc994e95df37ac22778e63fd72cd")
    version("develop", branch="develop", get_full_repo=True)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v09_81_00d00.patch', when='@09_81_00d00')

    depends_on("dunedataprep")
    depends_on("duneexamples")
    depends_on("protoduneana")
    depends_on("nurandom")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ] 
        return args

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
