#Set methods

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(f"Set 1: {s1}")
print(f"Set 2: {s2}")
#Union
s3 = s1.union(s2)
print(f"Union set: {s3}")
#This will return all the elements present in both the sets.

#Intersection
s4 = s1.intersection(s2)
print(f"Intersection set: {s4}")
#This will return the common elements present in both the sets.

#Intersection_update
s1.intersection_update(s2)
print(f"Intersection update set: {s1}")
#This will update the set s1 with the common elements present in both the sets.

#Difference
s5 = s1.difference(s2)
print(f"Difference set: {s5}")
#This will return the elements that are in s1 but not in s2.

#Difference_update
s1.difference_update(s2)
print(f"Difference update set: {s1}")
#This will update the set s1 with the elements that are in s1 but not in s2.

#Symmetric difference
s6 = s1.symmetric_difference(s2)
print(f"Symmetric difference set: {s6}")
#This will return the elements that are not common in both the sets.

#Symmetric_difference_update
s1.symmetric_difference_update(s2)
print(f"Symmetric difference update set: {s1}")
#This will update the set s1 with the elements that are not common in both the sets.

#Update
s1.update(s2)
print(f"Updated set: {s1}")
#This will update the set s1 with the values of s2.

#Set methods
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8, 9}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

#1. isdisjoint
#This methods checks if items of given set are present in another set.
#If they are present, it returns False else True.
print(f"Is disjoint: {set1.disjoint(set2)}")
#This will return False as 5 is present in both the sets.

#2. issuperset
#This method checks if all the items of a given set are present in original set. Returns True if yes else False.
print(f"Is superset: {set1.issuperset(set2)}")
#This will return False as all the items of set2 are not present in set1.

#3. issubset
#This method checks if all the items of a given set are present in original set. Returns True if yes else False.
print(f"Is subset: {set1.issubset(set2)}")
#This will return False as all the items of set1 are not present in set2.

#4. pop
#This method removes a random item from the set.
print(f"Pop: {set1.pop()}")
#This will remove a random item from the set.

#5. remove
#This method removes the specified item from the set.
set1.remove(4)
print(f"Remove: {set1}")
#This will remove the item 4 from the set.

#6. clear
#This method removes all the items from the set.
set1.clear()
print(f"Clear: {set1}")
#This will remove all the items from the set.

#7. copy
#This method copies the set to another set.
set3 = set2.copy()
print(f"Copy: {set3}")
#This will copy the set2 to set3.

#8. add
#This method adds an item to the set.
set2.add(10)
print(f"Add: {set2}")
#This will add the item 10 to the set.

#9. discard
#This method removes the specified item from the set.
set2.discard(10)
print(f"Discard: {set2}")
#This will remove the item 10 from the set.

