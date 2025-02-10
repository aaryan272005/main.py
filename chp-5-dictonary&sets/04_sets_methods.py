s = {1, 2, 3, 4 , 45,344,2,34,"Aaryan"}
print(type(s))
s.add("Sherkhane") 
print(s)  # Output: {1, 2, 3, 4, 34, 45, 344}

'''Properties of Sets'''
#1. Unordered : Sets order doesn't matter
#2. Unindexed: cannot access elements by index
#3. Their is no way to change items in sets 
#4. Sets cannot contain duplicates values

''' Operation in sets '''
#Consider the following set

s = {1, 8, 2, 3}

#1.lens(s) : returns 4 the length of the set 
#2.s.remove(8) : update the set s and remove 8 from s 
#3.s.pop() : Removes an abitiary element from the set and return the element removed 
#4.s.clear() : removes all elements from the set
#5.s.union({8,11}) : returns a new set with all items from both the sets {1,8,2,3,11}
#6.s.intersection({8,11}) : returns a set which contains only items in both elements 
#7. set.add(3)              # Adds an element to the set
#8. set.copy()                 # Returns a shallow copy of the set
#9. set.difference({8:11})  # Returns a set with elements in the set but not in {8:11}
#10. set.difference_update({8:11})  # Removes elements in the set that are also in {8:11}
#11. set.discard(3)          # Removes an element from the set if it exists (does not raise KeyError)
#12. set.intersection_update({8:11})  # Updates the set to only contain elements common to both sets
#13. set.isdisjoint({8:11})  # Returns True if no elements are common to both sets
#14. set.issubset({8:11})    # Returns True if all elements of the set are in {8:11}
#15. set.issuperset({8:11})  # Returns True if all elements of {8:11} are in the set
#16. set.symmetric_difference({8:11})  # Returns a set with elements in either set but not both
#17. set.symmetric_difference_update({8:11})  # Updates the set with elements in either set but not both
#18. set.update({8:11})      # Updates the set with elements from {8:11}
