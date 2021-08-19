from collections import Counter

print(Counter(['B','B','A','B','C','A','B','B','A','C']))
for i in Counter(['B','B','A','B','C','A','B','B','A','C']).elements():
    print(i)
print(Counter(['B','B','A','B','C','A','B','B','A','C']).most_common(2))