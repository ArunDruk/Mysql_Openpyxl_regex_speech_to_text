
L1=[4,2,8,9,6]
L2= L1.copy()


for i in range(len(L1)+1):
    for j in range(i+1,len(L1)):
        if L1[i] > L1[j]: # for Descending order if l1[i] < l1[j]

            L1[i],L1[j]=L1[j],L1[i]

print("Original List = ", L2)
print("Ordered List = ",L1)