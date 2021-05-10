"""This file contains a solution for a prime based coding test.

It is a variation on the sieve of Eratosthenes.

Sift the Two's and Sift the Three's,
The Sieve of Eratosthenes.
When the multiples sublime,
The numbers that remain are Prime.

https://en.wikipedia.org/wiki/Eratosthenes
"""
from itertools import compress


def prime_solution(starting_number: int):
    """
    Return a list of primes.

    Note if the number submitted is a prime it will not be returned as we are looking
    for primes less than that number.
    :param starting_number: the upper bound of our search
    :return: primes: a list of primes
    """
    primes = []
    if type(starting_number) is not int:
        raise ValueError(" This system requires an integer.")
    # check for negative
    if starting_number < 1:
        raise ValueError(" This system requires an valid positive integer.")
    # 1 is not a prime we can immediately return an empty list.
    # If the starting number is 2 we can immediately return an empty list
    # as we are returning primes less than 2 and there are none.
    if starting_number <= 3:
        return primes

    # there are multiple possible solutions I have gone with the sieve of Eratosthenes
    primes = [True for number in range(starting_number)]
    # zero is not a prime
    primes[0] = False
    # 1 is not a prime
    primes[1] = False

    prime = 2
    while (prime * prime) <= starting_number:
        #  if this has not changed, it is a prime
        if primes[prime]:
            # its multiples should be updated as they are not primes
            for i in range(prime * 2, starting_number, prime):
                primes[i] = False
        prime += 1

    #  compress is more efficient for bigger lists
    all_primes = list(compress(range(len(primes)), primes))
    # todo add logging
    print(all_primes)
    return all_primes


if __name__ == "__main__":
    # change this if you wish
    start_number = 30
    prime_solution(start_number)