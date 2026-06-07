import pytest

from fastexp import fastexp

CASES = [
    pytest.param(2, 0, 1, id="n_zero"),
    pytest.param(0, 0, 1, id="zero_zero"),
    pytest.param(2, 1, 2, id="n_one"),
    pytest.param(0, 5, 0, id="base_zero"),
    pytest.param(1, 1000, 1, id="base_one"),
    pytest.param(-1, 7, -1, id="neg_one_odd"),
    pytest.param(-1, 8, 1, id="neg_one_even"),
    pytest.param(2, 10, 1024, id="power_of_two"),
    pytest.param(3, 13, 1594323, id="odd_exponent"),
    pytest.param(-2, 5, -32, id="neg_base_odd"),
    pytest.param(-2, 6, 64, id="neg_base_even"),
    pytest.param(7, 20, 7**20, id="large"),
]


@pytest.mark.parametrize("x,n,expected", CASES)
def test_fastexp(x, n, expected):
    assert fastexp(x, n) == expected


@pytest.mark.parametrize("x", [2, 3, -4, 0, 1])
@pytest.mark.parametrize("n", range(0, 12))
def test_matches_builtin(x, n):
    assert fastexp(x, n) == x**n


def test_does_not_mutate_via_aliasing():
    # x and n are ints (immutable), but guard against future
    # refactors that might accidentally rebind the caller's args.
    x, n = 5, 6
    fastexp(x, n)
    assert (x, n) == (5, 6)


def test_negative_exponent_returns_one():
    # Current behavior: the while-loop guard skips negative n.
    # Pinning this so a future change is a deliberate choice.
    assert fastexp(2, -3) == 1
