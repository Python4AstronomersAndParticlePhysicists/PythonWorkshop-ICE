import pytest
from factorial import factorial


def test_n_between_1_and_5():
    correct_factorials = {1: 1,
                          2: 2,
                          3: 6,
                          4: 24,
                          5: 120}
    for n, expected in correct_factorials.items():
        assert factorial(n) == expected


def test_n_zero():
    assert factorial(0) == 1


def test_n_negative():
    with pytest.raises(ValueError):
        factorial(-1)
