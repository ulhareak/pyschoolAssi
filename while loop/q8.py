"""Create a function that takes in a positive integer and return a list of prime numbers.
A prime number is only divisible by 1 and itself."""


def primeNumbers(num):
    primes = []
    i = 2
    # iterates through range from 2 to num(inclusive)
    while i <= num:     # add 'while' condition
        k = 2
        isPrime = True
        # check if prime number
        while k < i:      # add 'while' condition
            if i % k == 0:
                isPrime = False
            k += 1            # update k
        if isPrime:
            primes.append(i)

        i += 1               # update i
    return primes


if __name__ == "__main__":
    print(primeNumbers(5))
    print(primeNumbers(1))
