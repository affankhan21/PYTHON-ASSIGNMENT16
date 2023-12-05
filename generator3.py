def myrange (start=0,stop=None,step=1):
    cur=start
    while cur<stop:
        yield cur
        cur+=step
num=list(myrange(3,33,3))
print(num)        