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
#     spack install duneutil
#
# You can edit this file again by typing:
#
#     spack edit duneutil
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Duneutil(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/duneutil/archive/refs/tags/v10_08_02d00.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("10_08_02d00", sha256="41666f3e06f5f5b9c36ac8c38b7578fd38a92f6fb16b94196c0e58da8af462b9")
    version("10_00_03d00", sha256="883877e913a99590a05f18d2d212cbf63d6ae3e574f094aeda4d72887c700d1d")
    version("09_92_00d00", sha256="fc0cb55678361a3488a17769cfcbe101ca1f513e8748261beb67caf86fb3974b")
    version("09_89_01d01", sha256="e7f451fb6409afb261d5ad8b1a4381e7410db338dd2c601f688cda6164f5492f")
    version("09_81_00d00", sha256="3cd857e366c7ecf1648f0f7aa76c2821ba25fe8b8d702ff47e2d7291d006a3bf")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v09_81_00d00.patch', when='@9_81_00d00')

    # FIXME: Add dependencies if required.
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("art-root-io")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ] 
        return args

