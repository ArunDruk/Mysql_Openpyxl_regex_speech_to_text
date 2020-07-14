#a="5556655444"
# a="5556"
# a="8763344"
# a="9874432"
# a="7755669999"
a="aabbde"
L=list(a)
L1=set(L)
# print(len(L1))
# print(len(L))
i=0
j=1
for k in range(len(L1)):
    inc=1

    if (j < len(a) and a[i] == a[j]):
        while(j!=len(a) and a[i] == a[j]):
            inc+=1
            i+=1
            j+=1
        L.insert(j+k,inc)

    else:
        L.insert(j+k,inc)
    i+=1
    j+=1

s="".join(str(l) for l in L)
print(f"Given String is {a}")
print(f"Output counting the occurances of each given digit {s}")