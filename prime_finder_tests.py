"""Test for the prime finder function."""
import pytest

from prime_finder import prime_solution


def test_prime_solution():
    """A test of the solution to the prime conundrum.

    Output:
    A list of all prime numbers which are smaller than the input-number.
    E.g.
      If input is 5
        Output is: 2, 3
      If input is 6
        Output is: 2, 3, 5
    """
    with pytest.raises(ValueError):
        prime_solution("Iamastring")
    with pytest.raises(ValueError):
        prime_solution(-1)

    assert prime_solution(1) == []
    assert prime_solution(2) == []
    assert prime_solution(3) == []
    assert prime_solution(5) == [2, 3]
    assert prime_solution(6) == [2, 3, 5]
    assert prime_solution(29) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert prime_solution(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert prime_solution(300000)[-1] == 299993
