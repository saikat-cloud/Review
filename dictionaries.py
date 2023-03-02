
# Dictionaries are written with curly brackets, and have keys and values

rollsroyce = {
    "brand": "Rolls Royce",
    "Founded" : "1906",
    "Owner" : "Rolls-Royce Holdings",
    "Successor" : "Automotive",
    "Headquarters" : "Derby",
    "Predecessor" : "Partnership",
    "Founders" : ["Henry","Royce","Charles","Rolls"]
}

# student = dict(name = "saikat", age = 29, country = "bangladesh")

# print(rollsroyce)
# print(len(rollsroyce))
# print(type(rollsroyce))

# #Access Dictionary Items

# print(rollsroyce["brand"])
# # get() that will give you the same result
# x = rollsroyce.get("brand")
# print(x)


# #Add a new item to the original dictionary
# rollsroyce["color"] = "white"
# print(rollsroyce)


# #The keys() method will return a list of all the keys in the dictionary
# x = rollsroyce.keys()
# print(x)

# #The values() method will return a list of all the values in the dictionary
# x = rollsroyce.values()
# print(x)

# #The items() method will return each item in a dictionary, as tuples in a list.
# x = student.items()
# print(x)



# #Can change the value of a specific item by referring to its key name
# student["name"] = "ant"
# print(student)

# #The update() method will update the dictionary with the items from the given argument
# student.update({"age" : "12"})
# print(student)

# #The pop() method removes the item with the specified key name
# student.pop("age")
# print(student)

# #The popitem() method removes the last inserted item
# student.popitem()
# print(student)

# #The del keyword removes the item with the specified key name
# del student ["country"]
# print(student)

# #The clear() method empties the dictionary
# student.clear()
# print(student)

# #Make a copy of a dictionary with the copy() or dict() method
# x = student.copy()
# print(x)


#Nested Dictionaries
# family = {
#   "c1" : {
#     "name" : "child1",
#     "year" : 2021
#   },
#   "c2" : {
#     "name" : "child2",
#     "year" : 2022
#   },
#   "c3" : {
#     "name" : "child3",
#     "year" : 2023
#   }
# }
# print(family)
# print(family["c2"]["year"])



# mur method

#   clear()	           Removes all the elements from the dictionary
#   copy()	           Returns a copy of the dictionary
#   fromkeys()	       Returns a dictionary with the specified keys and value
#   get()	           Returns the value of the specified key
#   items()	           Returns a list containing a tuple for each key value pair
#   keys()	           Returns a list containing the dictionary's keys
#   pop()	           Removes the element with the specified key
#   popitem()	       Removes the last inserted key-value pair
#   setdefault()	   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#   update()	       Updates the dictionary with the specified key-value pairs
#   values()	       Returns a list of all the values in the dictionary








# student = {
#     "name" : "saikat",
#     "age" : 28,
#     "country" : "bangladesh"
# }

# print(student["country"])

# student.update({"towen":"Dhaka"})
# print(student)

# student.pop([1])
# print(student)
