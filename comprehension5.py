sentence = input("ENTER THE SENTENCE :")

ex = sentence.split()

result = [w for w in ex if len(w) <5]
print(result)