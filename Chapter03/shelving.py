import shelve

class ShelvedClass:
    def __init__(self, name):
        self.name = name

my_list = ['a','b','c']

my_dictionary = {
    'a': ShelvedClass('First'),
    'b': ShelvedClass('Second'),
    'c': ShelvedClass('Third'),
}

file = shelve.open('shelved.shelve')
file['class'] = ShelvedClass('ECCouncil')
file['list'] = my_list
file['dictionary'] = my_dictionary
file.close()