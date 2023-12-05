def fibo_generator():
    a,b=0,1
    while(True):
        yield a
        a,b=b,a+b
a=fibo_generator()
for i in range(20):
    print(next(a))
