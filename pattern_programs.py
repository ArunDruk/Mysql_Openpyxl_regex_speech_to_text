#### \r, this is a carriage return. A carriage return returns the cursor to the beginning of the same line, and a newline moves the cursor down by one line.
##### Reference https://medium.com/edureka/python-pattern-programs-75e1e764a42f
# n=5
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=" ")
#         print("\r")
######################################### Star Pattern - Pyramid shape ###########################################################
# def pattern(n):
#
#     k = 2 * n - 2   # This gives the initial spacing distance here 8 whitespaces.
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print("\r")
#
#
# pattern(5)

################################################# Star Pattern -  Reverse Pyramid shape ###################################################
# def pattern(n):
#
#     k = 2 * n - 2   # This gives the initial spacing distance here 8 whitespaces.
#     for i in range(n-1,-1,-1):
#         for j in range(0, k):
#             print(end=" ")
#         k = k + 1
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print("\r")
#
#
# pattern(5)

################################################# Star Pattern - Hour Glass Pattern #################################################

# def pattern(n):
#
#     k = 2 * n - 2   # This gives the initial spacing distance here 8 whitespaces.
#     for i in range(n-1,-1,-1):
#         for j in range(0, k):
#             print(end=" ")
#         k = k + 1
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print("\r")
#
#     # k = 2 * n + 2  # This gives the initial spacing distance here 8 whitespaces.
#     for i in range(0, n):
#         for j in range(0, k-1):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print("\r")
#
# pattern(7)

################################################# Characters - Rangoli Pattern #################################################
# Reference https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string


def pattern(n):
    chars = string.ascii_lowercase
    sub_char=chars[:n]
    k = 2 * n - 2  # This gives the initial spacing distance here 8 whitespaces.
    for i in range(0, n):
        for j in range(0, k-1):
            print(end="-")
        k = k - 1
        for j in range(0, i + 1):
            print(sub_char[-i], end="-")
        for j in range(0, k):
            print(end="-")
        print("\r")

    # k = 2 * n - 2  # This gives the initial spacing distance here 8 whitespaces.
    for i in range(n - 1, -1, -1):
        for j in range(0, k):
            print(end="-")
        k = k + 1
        for j in range(0, i + 1):
            print(sub_char[-i], end="-")
        for j in range(0, k-1):
            print(end="-")
        print("\r")

pattern(4)