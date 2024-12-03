from mwm import fmath
from mwm import pymath

class TestClass:

    def test_fmath(self):
        assert fmath.fadd(3.1, 4) == 7.1
        assert fmath.fmult(3.1, 4) == 12.4

    def test_pymath(self):
        assert pymath.pyadd(3.1, 4) == 7.1
        assert pymath.pymult(3.1, 4) == 12.4
