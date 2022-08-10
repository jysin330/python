#creating empty set
b = set()
print(type(b))
# adding values to an empty set
b.add(2)
b.add(4)
b.add(3) # adding a value repeatedly does not changes a set
# b.add([34,56,7])  #cannot add list or dictionary to sets --> not hashable
# b.add({3:4})  #cannot add list or dictionary to sets--->--> not hashable
b.add((34,56,7))  
print(b)
#length of the set
print(len(b)) #prints the length of this set
# removal of items
# b.remove(2) #remove 2 from set b
# b.remove(29) # trows an error while to remove 20 (which is not present in set b)
print(b)
# b.pop()
# print(b)
# # b.clear()
b.union({8,9})
print(b)