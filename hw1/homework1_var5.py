input_a = input('Введите число а: ')
input_b = input('Введите число b: ')
input_c = input('Введите число c: ')

a = float(input_a)
b = float(input_b)
c = float(input_c)

if a*b == c:
    print('Произведение a и b дает c')
else:
    print('Произведение a и b НЕ дает c')

if b == 0:
    print('На ноль делить нельзя!')
elif a/b == c:
    print('Если a разделить на b, получится c')
else:
    print('Если a разделить на b, c НЕ получится :(')

print('End.')