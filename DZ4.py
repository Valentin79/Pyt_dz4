#=========================== Задача 1 ================================
# 1.	Дан список чисел. Создать список, в который попадают числа,
#  описываемые возрастающую последовательность. 
#  Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
#  Порядок элементов менять нельзя
# Примечание: плохо понял условие задачи, и нет ли тут ошибки в примере?
# Просто сделал возрастающие без всяких прочих условий последовательности.

# num_list = [1, 5, 2, 3, 4, 6, 1, 7]
# itr = 0 # счетчик итераций нужен для вывода последнего результата
# count = 1 # счетчик результатов
# res = [num_list[0]]
# for i in num_list:
#     flag = False
#     itr += 1
#     if i > max(res):
#         res.append(i) # добавляем следующее число к результату
#         flag = True # следующую сторку пропускаем
#     if flag == False and len(res) > 1: 
#         print(f'{count}: {res}') # выводим результат
#         count += 1
#         res = [i] # обнуляем результат и добавляем в него число с текщим индексом
#     if i < res[0]: res[0] = i # если в исходном списке есть нисходящая последовательность
#     if itr == len(num_list): print(f'{count}: {res}') # последний результат

#=========================== Задача 2 ================================

# 2.	Создать и заполнить файл случайными целыми значениями.
#  Выполнить сортировку содержимого файла по возрастанию. 

# import random

# def write_random_nums(n): # Записываем n случайных чисел
#     with open('file1.txt', 'w') as data:
#         for i in range(n):
#             data.write (str(random.randint(0, 100))+ ' ')
            
# def bubble_sort (n): # сортировка пузырьком
#     nums = list(map(int, n.split(" "))) # список, что бы программа не капризничала
#     swap = True 
#     while(swap): 
#         swap = False 
#         for i in range(len(nums) - 1): 
#             if nums[i] > nums[i+1]: 
#                 nums[i], nums[i+1] = nums[i+1], nums[i] 
#                 swap = True 
#     return nums

# n = 10
# write_random_nums(n)

# path = 'file1.txt'
# data = open(path, 'r') # считываем файл
# for line in data:
#     print(line)
# data.close()
# line = line[: -1] # удаляем последний символ (пробел), что бы программа не капризничала

# result_list = bubble_sort(line) # получаем отсортированный список
# result = str(result_list) # переводим его в стррку
# result = result.replace(',', '')
# result = result.replace('[', '')
# result = result.replace(']', '') # и я не знаю, можно ли это сделать лаконичнее
# print(result)
# with open('file1.txt', 'w') as data:
#     data.write(result) # переписываем файл

#=========================== Задача 3 ================================

#  найти триплеты и просто выводить их на экран.
#  Триплетом называются три числа, которые в сумме дают 0. 

# import time
# num_list = []
# path = '1Kints.txt'
# data = open(path, 'r') 
# for line in data:
#     num_list.append([int(line)])
# data.close()
# i = 0
# j = 0
# k = 0
# lenght = len(num_list)
# while i < lenght:
#     j = i + 1
#     while j < lenght:
#         k = j+1
#         while k < lenght:
#             print(f'{lenght}: k= {k} j= {j} i= {i}, {num_list[i]} , {num_list[j]} , {num_list[k]}')
#             if num_list[i] + num_list[j] + num_list[k] == 0:
#                 print(f'{num_list[i]} + {num_list[j]} + {num_list[k]} = 0')
#                 time.sleep(5)
#             k+=1
#         j+=1
#     i+=1