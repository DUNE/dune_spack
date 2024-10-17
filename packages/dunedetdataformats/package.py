# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Dunedetdataformats(Package):
    """Dunedetdataformats"""

    version("4_4_0", sha256="1312f255869f6b021df8c9a7885925192e62094f46808d3b7f6bd99d6efc0a20")
    version("4_1_0", sha256="479de5f1392b6303c258bced663b9aebd22ccd4a0aab2dd2910a9e1e295808b8")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, self.spec.prefix)
