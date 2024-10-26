#A program to imply set methods with user input.
#The main aim of this program is to try out writing a program in a professional way.

#Initial sets
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

#Function for union set operation.
def union(set1, set2):
    '''The union set returns all the items(non repeating) from both the sets.'''
    print(union.__doc__)
    set3 = set1.union(set2)
    return set3
#Function for intersection set operation.
def intersection(set1, set2):
    '''The intersectin set returns the items that are present in both the sets.'''
    print(intersection.__doc__)
    set4 = set1.intersection(set2)
    return set4
#Function for difference set operation.
def difference(set1, set2):
    '''The difference set returns the items from set 1 only.'''
    print(difference.__doc__)
    set5 = set1.difference(set2)
    return set5
#Function for symmetric difference set operation.
def symmetric_difference(set1, set2):
    '''The symmetric difference set returns the items that aren't common in both the sets.'''
    print(symmetric_difference.__doc__)
    set6 = set1.symmetric_difference(set2)
    return set6
#Function for update set.
def update(set1, set2):
    '''The update set returns the updated set, set1 with the items of set2.'''
    print(update.__doc__)
    set1 = set1.update(set2)
    return set1

#Function to display user menu.
def user_menu():
 print(f"The sets are: {set1} and {set2}")
 print("1. Union")
 print("2. Intersection")
 print("3. Difference")
 print("4. Symmetric Difference")
 print("5. Update")
 print("Press 0 to quit")
 choice = int(input("Enter your choice:"))

#Function for main program logic.
def set_choice():
 while choice != 0:
     match choice:
         case 1:
             print(f"Set after operation: {union(set1, set2)}")
         case 2:
             print(f"Set after operation: {intersection(set1, set2)}")
         case 3:
             print(f"Set after operation: {difference(set1, set2)}")
         case 4:
             print(f"Set after operation: {symmetric_difference(set1, set2)}")
         case 5:
             print(f"Set after operation: {update(set1, set2)}")
         case _:
             print("Invalid choice. Please try again.")
     choice = int(input("Enter your choice:"))
 print("Quitting...")