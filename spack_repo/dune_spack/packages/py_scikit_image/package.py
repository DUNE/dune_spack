from spack_repo.builtin.packages.py_scikit_image.package import (
    PyScikitImage as BuiltinPyScikitImage,
)

from spack.package import *


class PyScikitImage(BuiltinPyScikitImage):
    """Builtin py-scikit-image, buildable with setuptools 60+ for 0.18.

    scikit-image 0.18 builds with numpy.distutils, which imports
    distutils.msvccompiler. setuptools 60+ replaces the stdlib distutils with
    its own copy, and 74+ removed msvccompiler from it. dunesw ships
    setuptools 79 and py-networkx 2.7.1, which caps scikit-image below 0.20,
    so 0.18.3 is the version that fits. On Python 3.11 the stdlib distutils
    is still present; tell setuptools to use it.
    """

    def setup_build_environment(self, env):
        if self.spec.satisfies("@:0.19 ^python@:3.11"):
            env.set("SETUPTOOLS_USE_DISTUTILS", "stdlib")
