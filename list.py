
#Lists are used to store multiple items in a single variable

fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
andfruit = list(("blackcurrant", "watermelon"))
number = [12,11,28,38,64,43,90,9,72]

# #Access List Items
# print(fruit[1])
# print(fruit[-1])
# print(fruit[2:-1])
# print(fruit[3:])



#Change Item Value

# #To change the value of a specific item
# fruit[1] = "blackcurrant"       
# print(fruit)

# #To change the value of items within a specific range
# fruit[1:3] = ["blackcurrant", "watermelon"]
# print(fruit)



#Add List Items

# #To insert a list item at a specified index
# fruit.insert(1,"blackcurrant")
# print(fruit)

# #To add an item to the end of the list
# fruit.append("watermelon")
# print(fruit)

# # To append elements from another list to the current list, use the extend()
# fruit.extend(andfruit)
# print(fruit)



#Remove Specified Item

#The remove() method removes the specified item.
# fruit.remove("apple")
# print(fruit)

# #The pop() method removes the specified index
# fruit.pop(0)
# print(fruit)

# #The del keyword also removes the specified index
# del fruit[0]
# print(fruit)

# #The clear() method empties the list
# fruit.clear()
# print()



#Sort Lists

# #List objects have a sort() method that will sort the list alphanumerically
# fruit.sort()
# print(fruit)

# number.sort()
# print(number)


# #The function will return a number that will be used to sort the list
# def usekey(n):
#   return abs(n - 90)    #want short use small number

# number = [12,11,28,38,64,43,90,9,72]
# number.sort(key = usekey)
# print(number)



# Copy a List

# # Make a copy of a list with the copy() method
# myfruits = fruit.copy()
# print(myfruits)

# # Another way to make a copy is to use the built-in method list()
# myfruits = list(fruit)
# print(myfruits)



# # Join Two Lists
# joinlist = andfruit + number
# print(joinlist)

# #use the extend() method, which purpose is to add elements from one list to another list
# number.extend(andfruit)
# print(number)



# mur Methods

    #   append()	    Adds an element at the end of the list
    #   clear()	        Removes all the elements from the list
    #   copy()	        Returns a copy of the list
    #   count()	        Returns the number of elements with the specified value
    #   extend()	    Add the elements of a list (or any iterable), to the end of the current list
    #   index()	        Returns the index of the first element with the specified value
    #   insert()    	Adds an element at the specified position
    #   pop()	        Removes the element at the specified position
    #   remove()    	Removes the item with the specified value
    #   reverse()   	Reverses the order of the list
    #   sort()	        Sorts the list