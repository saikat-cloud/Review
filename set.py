
#Set items are unchangeable, but I can remove items and add new items.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Duplicates Not Allowed
# Unchangeable
# Unordered - the items in a set do not have a defined order.


fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
number = {1,2,3,4,5,6,7}


# # Check if "banana" is present in the set
# print("banana" in fruits)


# # add items from another set into the current set, use the update() method.
# fruits.update(number)       #update() can be any iterable object (tuples, lists, dictionaries etc.)
# print(fruits)


# #To remove an item in a set, use the remove(), or the discard() method.
# fruits.remove("apple")
# print(fruits)


# #Remove a random item by using the pop() method
# x = fruits.pop()
# print(x)
# print(fruits)

# #The clear() method empties the set
# fruits.clear()
# print(fruits)

# #The del keyword will delete the set completely
# del number
# print(number)


#Join Two Sets
# we can use the union() method that returns a new set containing all items from both sets, 
# or the update() method that inserts all the items from one set into another

jfruits = fruits.union(number)
print(jfruits)

# # add items from another set into the current set, use the update() method.
# fruits.update(number)       #update() can be any iterable object (tuples, lists, dictionaries etc.)
# print(fruits)



#mur Methods

#   add()	                Adds an element to the set
#   clear()         	    Removes all the elements from the set
#   copy()	                Returns a copy of the set
#   difference()	        Returns a set containing the difference between two or more sets
#   difference_update()	    Removes the items in this set that are also included in another, specified set
#   discard()	            Remove the specified item
#   intersection()	        Returns a set, that is the intersection of two other sets
#   intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#   isdisjoint()	        Returns whether two sets have a intersection or not
#   issubset()	            Returns whether another set contains this set or not
#   issuperset()	        Returns whether this set contains another set or not
#   pop()	                Removes an element from the set
#   remove()	            Removes the specified element
#   symmetric_difference()	Returns a set with the symmetric differences of two sets
#   symmetric_difference_update()	inserts the symmetric differences from this set and another
#   union()	                Return a set containing the union of sets
#   update()	            Update the set with the union of this set and others