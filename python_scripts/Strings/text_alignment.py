#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#up
for _ in range(thickness+1):
    print(''.ljust(thickness-int((thickness+1)/2)) + c*thickness + ''.ljust(thickness*3) + (c*thickness).rjust(thickness))

#midle
for _ in range(int((thickness+1)/2)):
    print(''.ljust(thickness-int((thickness+1)/2)) + c*thickness*5)

#down
for _ in range(thickness+1):
    print(''.ljust(thickness-int((thickness+1)/2)) + c*thickness + ''.ljust(thickness*3) + (c*thickness).rjust(thickness))

#Bottom Cone
for i in range(thickness-1, -1, -1):
    print((c*i).rjust(thickness*5 -1) + c + (c*i).ljust(thickness*4))