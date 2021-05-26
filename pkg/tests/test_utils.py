from pkg.utils import plus, minus, multi, intdiv, moddiv

def test_calc():
    assert plus(3, 4) == 7
    assert minus(5, 6) == -1
    assert multi(7, 8) == 56
    assert intdiv(10, 3) == 3
    assert moddiv(10, 3) == 1
