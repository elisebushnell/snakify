# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
y = int(input())
if y % 4 == 0 and y % 100 != 0:
    print('LEAP')
elif y % 400 == 0:
    print('LEAP')
else:
    print('COMMON')