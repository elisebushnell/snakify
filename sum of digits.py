# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
x = int(a%10)
y = int(.1*((a%100)-(a%10)))
z = int((a-(a%100))*.01)
b = int(x + y + z)
print(x + y + z)