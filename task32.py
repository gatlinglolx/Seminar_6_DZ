# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)

import random
arr = [random.randint(-50, 50) for i in range(random.randint(10,20))]
print(arr)
max = int(input("MAX= "))
min = int(input("MIN= "))
arr_1=[]
if max >= min:
   for i in range(len(arr)):
      if max >= arr[i] and min <= arr[i]:
         arr_1.append(i)
   print("Индексы:",arr_1)