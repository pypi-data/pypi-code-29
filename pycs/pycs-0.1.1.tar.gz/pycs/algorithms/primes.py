def primes_up_to(n):
    """Implements the sieve of Eratosthenes:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


    Parameters
    ----------
    n : Upper limit up to which (and including) prime numbers are
    returned

    Returns
    -------
    primes : list
        List of prime numbers up to n
    
    """
    if not isinstance(n, int):
        raise TypeError("n must be int")

    if n < 2:
        return []

    def regular_case(n):
        numbers = [True] * (n + 1)
        numbers[0] = numbers[1] = False

        for i, number in enumerate(numbers):
            if number:
                yield i
                for n in range(i * i, n + 1, i):
                    numbers[n] = False

    prime_numbers = list(regular_case(n))

    return prime_numbers
