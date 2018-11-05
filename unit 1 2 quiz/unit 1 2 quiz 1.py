name = str(input())
width = int(input())
depth = int(input())
length = int(input())
vol1 = width*depth*length
vol2 = (3.14*((width / 2)**2))*depth
gal1 = vol1*7.5
gal2 = vol2*5.875
print(name, gal1, 'gallons in a rectangular pool', gal2, 'gallons in a cyndrical pool')