"""This file contains a solution for a prime based coding test.

It is a variation on the sieve of Eratosthenes.

Sift the Two's and Sift the Three's,
The Sieve of Eratosthenes.
When the multiples sublime,
The numbers that remain are Prime.

https://en.wikipedia.org/wiki/Eratosthenes
"""
import time
from itertools import compress
from math import isqrt
import primesieve

import numpy as np


def prime_solution(starting_number: int):
    """
    Return a list of primes.

    Note if the number submitted is a prime it will not be returned as we are looking
    for primes less than that number.
    :param starting_number: the upper bound of our search
    :return: primes: a list of primes
    """
    if type(starting_number) is not int:
        raise ValueError(" This system requires an integer.")
    # check for negative
    if starting_number < 1:
        raise ValueError(" This system requires an valid positive integer.")
    # 1 is not a prime we can immediately return an empty list.
    # If the starting number is 2 we can immediately return an empty list
    # as we are returning primes less than 2 and there are none.
    primes = []
    if starting_number <= 3:
        return primes

    # there are multiple possible solutions I have gone with the sieve of Eratosthenes
    # user numpy here as it more efficiently builds large arrays
    primes = np.full(starting_number, True, dtype=bool)
    # zero is not a prime
    primes[0] = False
    # 1 is not a prime
    primes[1] = False

    # we only need to check up to the square root of the starting number to validate
    for prime in range(2, isqrt(starting_number) + 1):
        #  if this has not changed, it is a prime
        if primes[prime]:
            # its multiples should be updated as they are not primes
            for i in range(prime * 2, starting_number, prime):
                primes[i] = False

    #  compress is more efficient for bigger lists
    all_primes = list(compress(range(len(primes)), primes))
    # remove the print as it slows performance
    # print(all_primes)
    return all_primes

def get_primes(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n."""
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]

def get_primes_via_import(start_number):
    """use a package built for primes."""
    return primesieve.primes(start_number)


if __name__ == "__main__":
    # change this if you wish
    start = time.perf_counter()
    start_number = 30000000
    # prime_solution(start_number)
    # get_primes(start_number)
    get_primes_via_import(start_number)
    elapsed = time.perf_counter() - start
    print(elapsed)
