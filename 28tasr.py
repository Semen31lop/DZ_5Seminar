a=int(input('Введит число a: '))
b=int(input('Введит число b: '))
def sum(a, b):
    if b == 0:
            return a
    else:
            if b > 0:
                return sum(a + 1, b - 1)
    while a<0 or b<0:
        print(f'условия не верны')
        break 
print(sum(a,b))