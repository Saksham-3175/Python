#While loops are used to execute a block of statements repeatedly until a given condition is satisfied.

# for i in range(1,4):
#     print(i)

# while (i <= 3):
#     i += 1
#     print(i)
    
# print("The loop is exhausted.")
# As 11 is not less than or equal to 10, the loop is exhausted.

# a = int(input("Enter a number: "))
for a in range(0, 10):
 while (a < 10):
     if a == 5:
      print(f"loop breaked at {a}")
     break
#The above loop will run infinitely as the condition can always be true.
#If the number is repeated, print the number is repeated and break the loop.
# b = int(input("Enter a number: "))
# while (b < 10):
#     print(b)
#     if b == 5:
#         print("The number is repeated.")
#         break


#Random experiment.
# previous_numbers = []

# while True:
#     b = int(input("Enter a number (less than 10): "))
    
#     if b < 10:
#         if b in previous_numbers:
#             print(f"The loop is exhausted as {b} was repeated!")
#             break
#         else:
#             print(b)
#             previous_numbers.append(b)
#     else:
#         print("Please enter a number less than 10.")

#Decrementing while loop.
# num =  5
# while num > 0:
#     print(num)
#     num -= 1
#Else in while loop.
# else:
#     print("The loop is exhausted and under else.")
#The esle block is executed when the while loop is exhausted.

# count = -5
# while count > 0:
#     print(count)
#     count -= 1
# else:
#     print("Condition not met!")
#In the above while loop, the condition is not met as the count is less than 0.

#Do-while loop.
#Python does not have a do-while loop.
#Do-while loop executes the block of statements at least once.
#The condition is checked after the block of statement is executed.

#Emulation of do-while loop.
# num = 5
# while True:
#     print(num)
#     num -= 1
#     if num == 0:
#         break
#     else:
#         continue
#The loop will run at least once as the condition is checked after the block of statements is executed.
#however, the above code is not a good practice.
#The above code is not a good practice as it is not a good practice to use break and continue in the same loop.
#To avoid this, we can use a flag variable.

# num = 5
# flag = True
# while flag:
#     print(num)
#     num -= 1
#     if num == 0:
#         flag = False
#     else:
#         continue

