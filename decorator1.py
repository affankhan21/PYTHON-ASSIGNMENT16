def memoize(funct):
    cache=dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        res=funct(*args) 
        cache[args]=res
        return res
    return memoized_func
@memoize
def fibo(n):
    if n <2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(40))                  