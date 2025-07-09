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
#     spack install dunesw
#
# You can edit this file again by typing:
#
#     spack edit dunesw
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Dunesw(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/dunesw/archive/refs/tags/v09_89_01d01.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("10_08_02d00", sha256="d617560b80eadff1bac4e0b17a7ada47f187062341de83f6293e94126816f3dd")
    version("10_00_03d00", sha256="dbfc1dfa606a0c44152b39ae9f4efc5084436984dcbe00370da354c9f44fb966")
    version("09_92_00d00", sha256="0e3bae89b9e01f3b29303d5b65a72c5122c906e7f54c92ed9f282e13641d12c0")
    version("09_89_01d01", sha256="d516d3f7c00ed99fe23de77152bad556b5a6a24e777e3e5ec7d7a4beddaff3cb")
    version("09_81_00d01", sha256="126477cb91b6fd7a69ef2753505ca8dcd5739f4f509409cbf6f93f0774574862")
    version("09_81_00d00", sha256="f32da1e3e3ac4482674dcd3559c23a8acd10bc994e95df37ac22778e63fd72cd")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v09_81_00d00.patch', when='@09_81_00d00')

    # FIXME: Add dependencies if required.
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("duneana")
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
