string="This is Arun come Arun come-on Arun"

# L1=string.split(" ")
#
# for i in L1:
#     if i == "Arun":
#         print(f"Substring Arun found ")

for i in range(len(string)):
    if string.startswith("Arun",i):
        print(f"Substring found in position {i}")


