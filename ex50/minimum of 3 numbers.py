# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print(a)
if a < c < b:
    print(a)
if b < c < a:
    print(b)
if b < a < c:
    print(b)
if c < b < a:
    print(c)
if c < a < b:
    print(c)
if b == c:
    print(a)