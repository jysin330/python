mydict = {"ujala" : "light",
     "dabba": "box",
     "vastu":"item"
     }
print("option are", mydict.keys())
a=input("enter the hindi word\n")    
# print("the meaning of your word is:", mydict[a])
# below line will not throw an error if the key is not present in the dictonary --->
print("the meaning of your word is:", mydict.get(a))
