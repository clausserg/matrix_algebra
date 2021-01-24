"""
Unit and regression test for the matrix_algebra package.
"""

# Import package, test suite, and other packages as needed
import matrix_algebra
import pytest
import sys

def test_matrix_algebra_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "matrix_algebra" in sys.modules
