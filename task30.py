# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input())
d = int(input())
n = int(input())
progressive = [a1 + (n - 1) * d for n in range(1, n+1)]
print(progressive)

a1, d, n = map(int, input('a1 d n >').split())
p = [a1 + (n - 1) * d for n in range(1, n+1)]
print(p)