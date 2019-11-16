from distutils.core import setup

from SwaRaagam.userInterface.buildQt import BuildQt

cmdclass = {}
cmdclass['buildQt'] = BuildQt

setup(
    # ... other params here ...
    cmdclass=cmdclass,
)