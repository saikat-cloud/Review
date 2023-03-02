

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
andfruits = tuple(("blackcurrant", "watermelon"))
number = (1,2,3,4,5,6,7,8,9)

# #Access tuple Items
# print(fruits)
# print(fruits[1])
# print(fruits[-1])
# print(fruits[2:-1])
# print(fruits[3:])
# print(type(fruits))



# Update Tuples

# Add Items
# # Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
# x = list(fruits)
# x.append("watermelon")
# fruits = tuple(x)
# print (fruits)


# #Remove Items
# x = list(fruits)
# x.remove("apple")
# fruits = tuple(x)
# print(fruits)


# # Join Two Tuples
# jtuple = fruits + number
# print(jtuple)


# Multiply Tuples
mtuples = fruits * 3
print(mtuples)



# mur Methods

#    count()	Returns the number of times a specified value occurs in a tuple
#   index()	    Searches the tuple for a specified value and returns the position of where it was found