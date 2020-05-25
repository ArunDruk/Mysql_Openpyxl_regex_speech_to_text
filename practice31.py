# k="1864-ELEMENT"
# L=k.split("-")
# print(L[-1])

# L=["tc1543()","tc5983()","tc7821()"]
#
# for x in L:
#     comp_name=x[:-2]
#     print(comp_name)

class person():
    Name="Arun",
    Gender="Male"
    Age=30

a=getattr(person,"Gender")
print(a)