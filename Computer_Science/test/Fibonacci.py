

def fib(n):
    if(n < 2):
        return n
    else:
        return fib(n-1) + fib(n-2)


def ifib(n):
    if n < 2:
        return n
    else:
        n -= 1
        psum = 0
        sum = 1
        while n > 0:
            print(n)
            t = sum
            sum = psum + sum
            psum = t
            n -= 1
        return sum


def ifib2(n, psum, sum):
    if n < 2 and psum == 0:
        return n
    elif n > 1:
        return ifib2(n-1, sum, psum+sum)
    if n == 1:
        print(sum)
        return sum


ifib2(3, 0, 1)
