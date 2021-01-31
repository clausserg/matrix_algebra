"""
matrix_algebra
A module performing basic and complex matrix algebra, created while practicing Udemy courses
"""

# Add imports here
from .matrix_algebra import *
for matrix_algebra.matrix_operations import *
from .input_output import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
