my_dictionary = {'a':1,'b':2}

print(my_dictionary)
my_dictionary.update({'c':3})
print(my_dictionary)
my_dictionary.update({'a':9})
print(my_dictionary)
my_dictionary['d'] = 10
print(my_dictionary)

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
del my_dictionary['d']
print(my_dictionary)
a = [1,2,3]
my_dictionary['k'] = a
print(my_dictionary)
my_dictionary[a] = 'k'