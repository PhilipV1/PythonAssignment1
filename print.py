msg = "Knowledge is power!"
msgSplit = "Knowledge \n    is \n   Power!"
msgSqr = "="
msgBrack = "|"
width = len(msg) + 4


height = 5


print(msg)
print(msgSplit)


for y in range(height):
    for x in range(width):
        if((y != 0 and y != height - 1) and (x == 0 or x == width - 1)):
            print(msgBrack, end = '')
        elif(y == 0 or y == height - 1):
            print(msgSqr, end = '')
        elif(y == (height - 1)/2 and x >= 2 and x < width - 2):
            print(msg[x-2], end = '')
        else:
            print(' ', end = '')
    print()