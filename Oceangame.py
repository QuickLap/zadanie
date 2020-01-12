import time
import random
from tkinter import *


def create_ocean(F, size_i, size_j):  # Создание поля
    '''
    0 = ничего
    1 = скала
    2 = рыба
    3 = креветка
    '''
    for i in range(size_i):
        for j in range(size_j):
            F[i][j] = random.randint(0,3)
    return F


def show_ocean(F, size_i, size_j, canvas, root):  # Вывод поля на экран
    canvas.delete("all")
    d = {0:'blue', 1:'grey', 2:'green', 3:'orange'}
    step = 20
    f1 = f2 = 10
    for i in range(size_i):
        for j in range(size_j):
            item = F[i][j]
            canvas.create_rectangle(f1,f2,f1+step,f2+step, fill=d[item],outline='black')
            f1 += step
        f1 = 10
        f2 += step
    root.update()  #Ошибка явно связана с этим


def count_near(F, item, i, j, size_i, size_j):  #подсчет ячеек рядом
    k = 0
    if i>0:
        if F[i-1][j] == item:
            k += 1
    if j > 0:
        if F[i][j-1] == item:
            k += 1
    if i < size_i-1:
        if F[i+1][j] == item:
            k += 1
    if j < size_j-1:
        if F[i][j+1] == item:
            k += 1
    return k


def changed_ocean(F,size_i,size_j):  # Изменение океана по правилам игры
    F_new = F
    for i in range(size_i):
        for j in range(size_j):
            fish_near = count_near(F, 2, i, j, size_i, size_j)
            shrimp_near = count_near(F, 3, i, j, size_i, size_j)
            if F[i][j] == 1:  #скала
                pass

            elif F[i][j] == 0:  #пустота
                if fish_near == 3:
                    F_new[i][j] = 2
                elif shrimp_near == 3:
                    F_new[i][j] = 3

            elif F[i][j] == 2:  #рыба
                if fish_near == 3 or fish_near == 2:
                    pass
                else:
                    F_new[i][j] = 0

            elif F[i][j] == 3:  #креветка
                if shrimp_near == 3 or shrimp_near == 2:
                    pass
                else:
                    F_new[i][j] = 0
    return F_new


print('Введите размеры поля (Целые числа):')
print('длина = ', end='')
size_j = int(input())
print('ширина = ', end='')
size_i = int(input())
root = Tk()
canvas = Canvas(root, width=800, height=800)
canvas.pack()

ocean = [[0 for x in range(size_j)] for y in range(size_i)]

new_ocean = create_ocean(ocean, size_i, size_j)
show_ocean(new_ocean, size_i, size_j, canvas, root)
while True:
    new_ocean = changed_ocean(new_ocean, size_i, size_j)
    time.sleep(1)
    show_ocean(new_ocean, size_i, size_j, canvas, root)