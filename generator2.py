def palindrome(n):
    return str(n)==str(n)[::-1]
def genpalindrome(start):
    num=start
    while(True):
        if palindrome(num):
            yield num
        num+=1 
n=121
a=genpalindrome(n)
genpalindrome=next(a)
print(next(a))               