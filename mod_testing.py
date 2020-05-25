
##############################################################################################################
# class Person():
#   name = "John"
#   age = 36
#   country = "Norway"
#
# x = getattr(Person, 'age')
#
# D={'a':"Apple",'b':"Ball"}
# y=D.get('b',"KeyNotPresent")
# print(x)
# print(y)

##############################################################################################################
##############################################################################################################
file_name="CoStar_GL_IS_US_20191104160006.txt"
fr=open(file_name,"r")
lines=fr.readlines()
print(lines[0])
fr.seek(6,0)
# # old_inv_num=lines[1][16:31].strip()
# # old_inv_date=lines[1][34:42].strip()
# # print((lines[1][16:31]))
# fr.read()
# print(S)
lines=fr.readlines()
print(lines[0])
##############################################################################################################
# import datetime as DT
#
# print(DT.datetime.now())
# print(DT.datetime.now().strftime("%Y%m%d%H%M%S%f"))
##############################################################################################################
# def outer():
#     def inner():
#         print("inner")
#     inner()
#     print("Outer")
#
# outer()

# import traceback
# traceback.format_exc()