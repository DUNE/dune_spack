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
#     spack install dunedetdataformats
#
# You can edit this file again by typing:
#
#     spack edit dunedetdataformats
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Dunedetdataformats(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/dunedetdataformats/archive/refs/tags/v4_4_0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("4_4_4", sha256="ae4f18a4f3c09f503a0dca5373fb9b08ad04bfc4ead323605121ff3ec76a22df")
    version("4_4_0", sha256="1312f255869f6b021df8c9a7885925192e62094f46808d3b7f6bd99d6efc0a20")
    version("4_1_0", sha256="479de5f1392b6303c258bced663b9aebd22ccd4a0aab2dd2910a9e1e295808b8")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, self.spec.prefix)
