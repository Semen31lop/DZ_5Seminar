a=int(input('Введит число: '))
b=int(input('Введите степень числа: '))
def degree (m,n):
    step = m**n
    return step
print(degree(a,b))
#  Я  не понимаю какое решение вы хотели бы видеть , через эту рекурсию . у степени слишко много свойств .
#  А программа решит это даше с самым простым кодом как предсталенно выше .
a=int(input('Введит число: '))
b=int(input('Введите степень числа: '))
def pow(m,n):
    if n==0:
        return m
    else:
        return m**n
print(pow(a,b))
    