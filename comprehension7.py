div=[num for num in range(1,10001) if any (num %digit==0 for digit in range(1,10))]
print(div)