'''What will be the value of the following set 
    s = set()
    s.add(1)
    s.add(1.0)
    s.add('1') Length after this operation will be :'''
s = set()
s.add(1)
s.add(1.0) #Since 1 and 1.0 have the same value they are considered as one 
s.add('1')
print(len(s))