from mfm import fmath

class TestClass:

    def test_fmath(self):
        assert fmath.fadd(3.1, 4) == 7.1
        assert fmath.fmult(3.1, 4) == 12.4
