numbers=[]
for _ in range(5):
    num=float(input("Enter a num: "))
    numbers.append(num)

tuplenum = tuple(numbers)
print("Numbers entered: ",tuplenum)