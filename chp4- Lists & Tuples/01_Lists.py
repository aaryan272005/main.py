#Python list are containers to store a set of values of any data type
#NOTE: Unlike String/changes in the list are change within the list ,it doesn't create new list
L1=["apple","4","3.1427","orange","Aaryan"]

print(L1[0])
#Strings are imutable 
# we can make new String by using the existing String but cannot change the existing String
#but to do the change we can use list for example

L1[0] = "banana"
print(L1[0])
#NOTE: After changing it replaces the actual thing 
#NOTE: Unlike Strings,Lists are mutable

'''LIST INDEXING'''
print(L1[0]) #apple after replacing banana 
print(L1[1]) #4
print(L1[-1]) #Aaryan
print(L1[0:-1]) #[apple:Aaryan] #list slicing
