

# L1=[["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]
# L1=[["Harsh",20],["Beria",20],["Varun",19],["Kakunami",19],["Vikas",21]]  #o/p " Beria Harsh
L1=[["Sona",-25.001],["Mona",-25.0001],["Mini",-25.000],["Rita",-25.0]]

# L2=sorted(L1)
print(L1)
L1.sort(key= lambda x:x[1])
print(L1)
i=1
L1_duplicates=[]
for i in range(len(L1)):
    L1_duplicates.append(L1[i][1])

var1=L1_duplicates[0]
count=1

for i in range(1,len(L1_duplicates)):
    # j = i+1
    if (L1_duplicates[i] == var1):
        count+=1

L2=[]
i=1
for i in range(count,len(L1)):
    j=i+1
    if (j<len(L1) and L1[i][1] == L1[j][1]):
        L2.append(L1[i][0])
        L2.append(L1[j][0])

L2.sort()
for i in L2:
    print(i)
if len(L2) <=1:
    print(L1[1][0])

