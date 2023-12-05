str=input("ENTER THE STRING :")
vowels=["a","e","i","o","u"]
res="".join([i for i in str if i not in vowels])
print("THE RESULT IS :",res)