k = int(input())
x = k - 7*(k//7) 
if x < 3:
    print(x+3)
if x == 3:
    print(6)
if x == 4:
    print(0)
if x == 5:
    print(1)
if x == 6:
    print(2)
if k//7 == 0:
    print(3)
