# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Dunedaqdataformats(Package):
    """Dunedaqdataformats"""

    url = "https://github.com/DUNE/dunedaqdataformats/archive/refs/tags/v4_4_0.tar.gz"


    version("4_4_4", sha256="4806af70ae20295547fccefb70c93785a14e6b7a0ea1d3a2b7e94e3a47044988")
    version("4_4_0", sha256="fee0e31693c9fb6747cc252592f6442303c873d4d68ffb43c94a6ca049c97a9e")
    version("4_0_0", sha256="bdc50531cae25797f940c46b95b42f8ce2f285300c972a3baabf2930aa3da51e")
    version("develop", branch="develop", get_full_repo=True)

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, self.spec.prefix)
