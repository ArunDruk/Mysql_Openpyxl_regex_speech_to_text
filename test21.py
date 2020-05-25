# #L=[1,2,3,4,5]
# K=[623,657,698,765,742]
# K1=[]
#
# def adding_list(K):
#     m=1
#     for i in K:
#         K1.append(i+m)
#         m+=1
#     return K1
#
# mod_list=adding_list(K)
# print(mod_list)

from datetime import datetime

a=int(datetime.now().strftime("%Y%m%d%H%M%S%f")) #+int(index)

b=int(datetime.now().strftime("%Y%m%d%H%M%S"))
print(type(b))