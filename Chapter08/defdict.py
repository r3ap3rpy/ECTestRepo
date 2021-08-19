#__missing__(key) -> __getitem__()
from collections import defaultdict

dd = defaultdict(int)

L = range(20)

for i in L:
    dd[i]+=1
    
print(dd)