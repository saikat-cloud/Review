
# #A function is a block of code which only runs when it is called.

# def func(name):
#     print( name + " is my name")

# func("saikat")      #when it is called


#Number of Arguments
#By default, a function must be called with the correct number of arguments. 

# def name(fname , lname):
#     print(fname + lname + "is my name")

# #you have to call the function with 2 arguments, not more, and not less.
# name("Saikat", "Mondal")


# # Arbitrary Arguments, *args
# # If the number of arguments is unknown, add a * before the "parameter" name
# def name(*fmlname):
#     print(fmlname[2])

# name("Saikat","Kumar","Mondal")


# #Keyword Arguments
# #You can also send arguments with the key = value syntax
# def name (fname,mname,lname):
#     print("My first neme is " + fname)
#     print("my middle name is " + mname)
#     print("My last neme is " + lname)

# name(fname="Saikat", mname="Kumar", lname="Mondal")


# #Arbitrary Keyword Arguments, **kwargs
# def name (**funame):
#     print("my first name is " + funame["fname"])
#     print("my last name is "+ funame["lname"])

# name( fname = "Saikat", mname = "kumar", lname = "Mondal")


# #Default Parameter Value
# #f we call the function without argument, it uses the default value
# def dpcountry(country = "Bangladesh"):
#     print("I am from " + country)

# dpcountry()
# dpcountry("Canada")
# dpcountry("USA")
# dpcountry("UK")


# #Passing a List as an Argument
# def funct(food):
#     for x in food:
#         print(x)
# foods = ["vat", "mas", "dal"]
# funct(foods)


# #Return Values
# def rfunction(number):
#     return number + 2
# print(rfunction(4))



#The pass Statement
#function definitions cannot be empty, but some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def functio():
    pass

