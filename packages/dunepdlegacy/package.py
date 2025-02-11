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
#     spack install dunepdlegacy
#
# You can edit this file again by typing:
#
#     spack edit dunepdlegacy
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Dunepdlegacy(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/dunepdlegacy/archive/refs/tags/v1_01_05.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("1_01_05", sha256="60876ea0041c6054dba31789806d248bb9a2e74eec76bb90ae9711b6c8b86705")
    version("1_01_04", sha256="9662e6c2b3e7d4abc2d0e45ac249251359d6595e0a757ebb965521a9bcb043da")
    version("1_01_00", sha256="926130733ed28753ff637e52b120dc4ee669cf0a769e0d8f7049693670ee907a")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch('v1_01_05.patch', when='@1_01_05')
    patch('v09_81_00d00.patch', when='@1_01_00')

    # FIXME: Add dependencies if required.
    depends_on("gallery")
    depends_on("art")
    depends_on("artdaq-core")
    depends_on("cetlib")
    depends_on("nufinder")
    depends_on("messagefacility")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ] 
        return args

