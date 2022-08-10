mydict={
    "fast":"in a quick manner",
    "roshni":"light",
    "marks": [23,45,6],
    "anotherdict" :{"jyoti":"light",
    "roshni":"jyoti"},
     1:2
}
print(mydict.keys()) #print keys of the dictonary
# print(type(mydict.keys()))
# print(list(mydict.keys()))
print(mydict.values())
print(mydict.items()) #print (keys, values) for all contents of the dictonary
print(mydict)
updatedict={
    "rahul": "friend",
    "subham": "friend"
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("roshni")) #print value associated with key "roshni"
print(mydict["roshni"]) #print value associated with key "roshni"
#difference between .get and [] syntex in dictonary---->
print(mydict.get("roshni2")) #return none as roshni2 is not present in the dictionary
print(mydict("roshni2")) #throws an error as roshni2 is not present in the dictionary
