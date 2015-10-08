"""
project euler problem 7
the 10001st prime
"""

# The prime we're looking for
lastprime = 10001

# prime the pump so to speak
primes = [2,3,5]



def nth_prime(lastprime):
    """Checks naively if a number is a prime"""

    # the next candidate
    candidate = 4
    
    while (len(primes) < lastprime):
        isprime=True
        for x in primes:
            if candidate % x == 0:
                isprime=False
                break

        if isprime == True:
            primes.append(candidate)

        candidate = candidate + 1

    return primes[-1]

print (nth_prime(lastprime))
