
# def counter():
#     i=1
#     while i<5:
#         yield i
#         i+=1
#
# for i in counter():
#     print(i)

def squares(x):
    for i in range(x):
        yield i*i


L1= list(squares(6))
print(L1)