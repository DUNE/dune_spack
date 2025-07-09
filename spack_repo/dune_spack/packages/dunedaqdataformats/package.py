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
#     spack install dunedaqdataformats
#
# You can edit this file again by typing:
#
#     spack edit dunedaqdataformats
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Dunedaqdataformats(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/DUNE/dunedaqdataformats/archive/refs/tags/v4_4_0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("4_4_4", sha256="4806af70ae20295547fccefb70c93785a14e6b7a0ea1d3a2b7e94e3a47044988")
    version("4_4_0", sha256="fee0e31693c9fb6747cc252592f6442303c873d4d68ffb43c94a6ca049c97a9e")
    version("4_0_0", sha256="bdc50531cae25797f940c46b95b42f8ce2f285300c972a3baabf2930aa3da51e")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, self.spec.prefix)
