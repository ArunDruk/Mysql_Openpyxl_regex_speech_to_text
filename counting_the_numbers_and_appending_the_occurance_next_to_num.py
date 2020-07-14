

# def counting_num (a="55641",b=2):
#
#
#
#    return None
#
# counting_num("553221",3)


#a="5556655444"
# a="5556"
#a="8763344"
a="998874432"
L=list(a)
L1=set(L)
# print(len(L1))
# print(len(L))
i=0
j=1
for k in range(len(L1)):
    inc=1

    if (j < len(a) and a[i] == a[i+1]):
        while(j!=len(a) and a[i] == a[j]):
            inc+=1
            i+=1
            j+=1
        L.insert(j+k,inc)

    else:
        L.insert(j+k,inc)
    i+=1
    j+=1
    # if (a[i]==a[len(a)-1]):
    #     break
    # print(f"k = {k}")

s="".join(str(l) for l in L)
print(a)
print(s)
#print("Expected output 5553319111711121")

