# To print all the combinations of upto x,y,z and print in the list, exclude sum which is equal to n

x=1
y=1
z=1
n=2
L1=[]
[L1.append([i,j,k]) for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k != n)]

print(L1)