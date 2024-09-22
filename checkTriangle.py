a,b,c = map(int, input().split())

if a+b>c and a+c>b and b+c>a:
    print('this is valid triangle')
else:
    print("this is not a valid triangle") 