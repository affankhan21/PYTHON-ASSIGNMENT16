string13 = input("Enter the string :")
list11=[]
list11=string13.split()
print(list11)
word_freq=[list11.count(p) for p in list11]
print("The frequency of words is ...")
print(dict(zip(list11,word_freq)))