import sys

# sys.stderr.write("This is stderr text\n")
# sys.stderr.flush()
# sys.stdout.write("This is stdout text\n")
#
# print(sys.argv)  # This is going to print the path of the current file "print(sys.argv[0])"
# sys.argv , We can Pass the arguments when we execute this file in Terminal "python Sys_module_pgm1.py "Come on Arun"  "

def using_arguments(arg):
    print(arg)

if len(sys.argv) > 1:
    using_arguments(sys.argv[1])
else:
    print("No arguments passed")


