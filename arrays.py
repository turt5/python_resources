
array=[10,20,30,40,50,60]


# print array by loops
for i in array: 
    print("Array item: "+str(i))


array2=[
    "Apple",
    "Banana",
    "Mango",
    "Strawberry",
    "Lichi",
    "Pineapple",
]

print(len(array2)) # array length


# print array with index using loops
for index, value in enumerate(array2):
    print("Index: ",index,"Value: ",value)


array2.append("Grapes") # add item to array
print(array2)

array2.insert(0,"Orange") # insert item to array in specific index
print(array2)