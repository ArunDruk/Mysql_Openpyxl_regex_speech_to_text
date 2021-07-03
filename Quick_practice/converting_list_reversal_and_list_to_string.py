
a="This is for you Exclusively"
l=a.split(" ")
rev_l=[]
for i in range(len(l)):
    rev_l.insert(0,l[i])


# l=list(a)


print(rev_l)
print(type(rev_l))

s=str(" ".join(rev_l))
print(type(s))

print(s)