

# # single variable
# name = 'saikat'
# print(name)

# # multiple variable
# schoolName,age = str(input("enter your name  ")), int(input("enter your age  "))
# print("my name is ",schoolName,"and my age is ", age )


# Global Variables
vari = "riyad"
def gvariable():
    global vari
    # vari = "saikat"
gvariable()
print("my name is ", vari)