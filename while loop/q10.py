"""Create a function that computes the approximation of pi, based on the number of iterations specified."""


def piApprox(num):
    i = 1
    pi = 0
    in_ = 1
    while i <= num*2:                # set 'while' termination condition
        if(in_ % 2 == 1):
            pi += 4/i
        else:
            pi -= 4/i
        in_ += 1
        i += 2                       # update i
    return pi


if __name__ == "__main__":
    print(piApprox(1))
    print(piApprox(10))
    print(piApprox(100))
