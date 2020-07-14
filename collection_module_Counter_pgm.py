from collections import Counter

c1= Counter("Heellloooo")
c1.update("Arun")
print(c1)

print(c1['e'])

for char in c1.elements():
    print(char,end="\t")