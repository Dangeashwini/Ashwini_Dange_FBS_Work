def cache(fun):
    cache={}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result=fun(n)
        cache[n]=result
        return result
    return wrapper
        
@cache
def fib(n):
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)

n=int(input("Enter the number:"))
print(fib(n))

