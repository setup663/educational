import math
a = input("Введите сторону A:")
b = input("Введите сторону B:")
c = input("Введите сторону C:")

def ravnost(a, b, c):
    if (a == b == c):
        print('Треугольник ABC-равносторонний треугольник')

def ravnobed(a, b, c):
    if (a == b and a != c and b != c) or (c == b and c != a and b != a) or (c == a and c != b and b != a):
        print('Треугольник ABC-равнобедренный треугольник')
    else:
        ravnost(a, b, c)

def razn(a, b, c):
    if (a != b) and (a != c) and (b != c):
        print('Треугольник ABC-разносторонний')
    else:
        ravnobed(a, b, c)

def plos(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'площадь треугольника ABC: {round(s)}')
    razn(a, b, c)

def ori(a, b, c):
    if (a + b < c) or (a + c < b) or (c + b < a):
        print('сумма двух сторон меньше третьей')
    else:
        plos(a, b, c)

def Men(a, b, c):
    if  (a <= 0) or (b <= 0) or (c <= 0):
        print('одна из сторон меньше или равна нулю')
    else:
        ori(a, b, c)

def pr_str(a, b, c):
    if a.isdigit() == True and b.isdigit() == True and c.isdigit() == True:
        a = int(a)
        b = int(b)
        c = int(c)
        Men(a, b, c)
    else:
        print('вы ввели не числа')

if __name__ == "__main__":
    pr_str(a, b, c)