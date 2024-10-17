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
#     spack install duneopdet
#
# You can edit this file again by typing:
#
#     spack edit duneopdet
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from spack.pkg.fnal_art.fnal_github_package import *

import spack.util.spack_json as sjson

class Duneopdet(CMakePackage, FnalGithubPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/duneopdet/archive/refs/tags/v09_92_00d00.tar.gz"
    repo = "DUNE/duneopdet"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("09_92_00d00", sha256="6003147a6b8a0d943a9f11ceebc4ab2fbac48b9041ad78f560a7bd3ae27b4929")
    version("09_89_01d01", sha256="d39bf58d4dedf985f51d8b2d272354047603fc520145b282d17c85cd7877fdbe")
    version("09_81_00d00", sha256="ea4e39071507f9f1697ba2251481d2ff9396238a33ee38c0fe68070c2c1a9750")
    version("develop", branch="develop", get_full_repo=True)


    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v09_81_00d00.patch', when='@09_81_00d00')

    def patch(self):
        filter_file("LANGUAGES CXX", "LANGUAGES CXX C", "CMakeLists.txt")

    # FIXME: Add dependencies if required.
    depends_on("duneana")
    depends_on("dunecore")
    depends_on("nlohmann-json")
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
