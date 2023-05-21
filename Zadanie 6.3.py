a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
for c in range(a,b+1):
    if (c//3 == c/3 and c//5 == c/5):
        print('Fizz Buzz')
    elif c//5 == c/5:
        print('Buzz')
    elif c//3 == c/3:
        print('Fizz')
    else:
        print(c)