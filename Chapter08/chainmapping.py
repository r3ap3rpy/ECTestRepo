from collections import ChainMap

a = {'a':'Daniel','b':30,'c':2}
b = {'d':'Jack','e':20,'f':3}
c = {'g':'Joanne','h':40,'k':4}

combined = {}
combined.update(a)
combined.update(b)
combined.update(c)

d = ChainMap(a,b,c)
print(d)
print(combined)
print(d['a'])
print(combined['b'])