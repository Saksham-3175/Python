#Break
#A break statement is used to exit the loop immediately.
print("Break Statement:-")
for i in range(1, 11):
    print(f"2 * {i} = {2*i}")
    if i == 5:
        print(f"Broke the loop at {i}")
        break

#Continue
#A continue statement is used to skip the current iteration and continue with the next one.
print("\nContinue Statement:-")
for a in range(1, 11):
 if a == 5:
    print(f"Skipping {2 * a}")
    continue
 print(f"2 * {a} = {2*a}")

    