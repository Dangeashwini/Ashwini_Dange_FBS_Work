def fib(n):
    a=1
    b=0
    for i in range(1,n):
        c=a+b
        yield c
        a=b
        b=c
        
n=int(input("Enter the number:"))
res=fib(n)

print(next(res))
print(next(res))
    