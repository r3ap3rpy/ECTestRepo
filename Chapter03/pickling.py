import pickle 

class PickledClass:
    def __init__(self, name):
        self.name = name

def multiply(a, b):
    return a*b

my_list = [1,2,3,4,5,6,7,8,9,10]

my_dictionary = {
    'a' : 'one',
    'b' : 'two',
    'c' : 'three'
}

#file = open('pickled.pickle','wb')
#pickle.dump(PickledClass('ECCouncil'),file)
#pickle.dump(multiply, file)
#pickle.dump(my_list,file)
#pickle.dump(my_dictionary,file)
#file.close()

with open('pickled.pickle','wb') as file:
    pickle.dump(PickledClass('ECCouncil'),file)
    pickle.dump(multiply, file)
    pickle.dump(my_list,file)
    pickle.dump(my_dictionary,file)