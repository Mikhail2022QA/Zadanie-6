a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = 0
for d1 in range(a,b+1):
    print(d1,end = '\t')
print('\n')
for d2 in reversed(range(a,b+1)):
    print(d2, end = '\t')
print('\n')
for d3 in range(a,b+1):
    if d3//7 == d3/7:
        print(d3, end = '\t')
print('\n')
for d4 in range(a,b+1):
    if d4//5 == d4/5:
        c = c+1
print(c, end = '\t')