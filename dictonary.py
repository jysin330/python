mydict={
    "fast":"in a quick manner",
    "roshni":"light",
    "marks": [23,45,6],
    "anotherdict" :{"jyoti":"light",
    "roshni":"jyoti"}

}
print(mydict['fast'])
print(mydict['roshni'])
mydict['marks']= [34,56] #mutable--> u can change
print(mydict['marks'])
print(mydict['anotherdict'])
print(mydict['anotherdict']['jyoti'])