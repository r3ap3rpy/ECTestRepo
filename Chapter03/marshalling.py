import marshal

dictionary = {
    'Name' : 'Daniel',
    'Age' : 30,
    'Profession' : 'DevOps'
}

script = """
print("### Start of Marshal ###")
import this
for i in range(10):
    print(i)
print("### End of Marshal ###")
"""

code = compile(script,'<script>','exec')

#with open('execmarshal.marshal','wb') as exec_file:
#    marshal.dump(code, exec_file)

with open('execmarshal.marshal','rb') as exec_file:
    a = marshal.load(exec_file)

exec(a)


#with open('dictionary.marshall','wb') as dict_dump:
#    marshal.dump(dictionary, dict_dump)

#data = marshal.dumps(dictionary)
#print(repr(data))