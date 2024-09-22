x,y = map(int, input().split())

if x == 0 and y == 0:
    print('origin')
elif x == 0 and y != 0:
    print('y-axis')
elif x != 0 and y == 0:
    print('x-axis')
elif x > 0 and y > 0:
    print('1st quater')
elif x < 0 and y > 0:
    print('2nd quater')
elif x < 0 and y < 0:
    print('3rd quater')
elif x < 0 and y < 0:
    print('4th quater')
