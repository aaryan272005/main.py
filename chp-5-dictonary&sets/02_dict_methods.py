'''Dictionary Methods '''
#Consider the following dictionary

d={} # Empty dictionary

a={"key":"value",
   "Aaryan":"code",
   "marks":"100",
   "list":[1,2,3]}

# print(a.items()) # Returns a list of (keys/values) in the form of tuples
# print(a.keys()) # Returns a list of 'Contaning Dictionary keys' 
# print(a.values()) # Returns a list of 
# a.update({"name":"Aaryan", "surname":"sherkhane"})
print(a.get("name")) # Returns "Aaryan" 

#If Keys doesn't exist in the dictionary then :
print(a.get("surname")) # Returns None
print(a["surname"]) # Returns Error 

'''From CHAT GPT'''

# Python dictionary methods
seq = ["name", "form", "marks"]
value=a.get("value")
key= ["value", "form", "marks"]
default = a.get("default")

other_dict=dict
dict.clear()                # Removes all items from the dictionary
dict.copy()                 # Returns a shallow copy of the dictionary
dict.fromkeys(seq, value)   # Returns a new dictionary with keys from the sequence and values set to `value`
dict.get(key, default)      # Returns the value for the specified key, or `default` if not found
dict.items()                # Returns a view object of (key, value) tuple pairs
dict.keys()                 # Returns a view object displaying all the dictionary's keys
dict.pop(key, default)      # Removes and returns the item with the specified key, or `default` if not found
dict.popitem()              # Removes and returns an arbitrary key-value pair
dict.setdefault(key, default)  # Returns the value of the key if exists, otherwise inserts with `default` value
dict.update(other_dict)     # Updates the dictionary with items from another dictionary or iterable
dict.values()               # Returns a view object displaying all the dictionary's values
key in dict                 # Checks if a key exists in the dictionary