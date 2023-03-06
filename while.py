
# i = 1               #initialization
# while i < 10:       #while condition:
#     print(i)        #statements
#     i = i + 1       #update
                    

#With the break statement we can stop the loop even if the while condition is true
# i = 1
# while i < 10:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# #With the continue statement we can stop the current iteration, and continue with the next
# i = 1
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

#With the else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("i is no longer less than 10")