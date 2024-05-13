list=[10,10,20,30] #list can have duplicate values
set={30,30,50} #sets does not allow duplicate values



print(list)
print(set)



list.append(40) #add item to list
print(list)



list.pop() #remove last item from list
print(list)


list.pop(0) #remove item from list by index
print(list)


# set doesnot support indexing

set.add(40) #add item to set 
print(set)


set.add(90) #add duplicate item to set
print(set)


set.add(910) #add duplicate item to set
print(set)


set.remove(30) #remove item from set
print(set)