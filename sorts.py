from random import randint
import time
import matplotlib.pyplot as plt
import numpy as np
from sys import setrecursionlimit

#Сортировки
class Sort:

    def __init__(self, array):
        self.array = array


    def __str__(self):
        return f"{self.array}"


    def selection_sort(self):
        start_time = time.time()
        array_copy = self.array.copy()

        for target in range(len(array_copy)):
            min_index = target

            for index in range(target + 1, len(array_copy)):
                if array_copy[index] < array_copy[min_index]:
                    min_index = index

            if min_index != target:
                array_copy[target], array_copy[min_index] = array_copy[min_index], array_copy[target]

        return array_copy, (time.time() - start_time)


    def insertion_sort(self):
        start_time = time.time()
        array_copy = self.array.copy()

        for index in range(1, len(array_copy)):
            sort_ed = index - 1

            while sort_ed > -1 and array_copy[sort_ed] > array_copy[sort_ed + 1]:
                array_copy[sort_ed], array_copy[sort_ed + 1] = array_copy[sort_ed + 1], array_copy[sort_ed]
                sort_ed -= 1

        return array_copy, (time.time() - start_time)


    def exchange_sort(self):
        start_time = time.time()
        array_copy = self.array.copy()

        for border in range(len(array_copy) - 1):
            for index in range(len(array_copy) - 1 - border):
                if array_copy[index] > array_copy[index + 1]:
                    array_copy[index], array_copy[index + 1] = array_copy[index + 1], array_copy[index]

        return array_copy, (time.time() - start_time)


    def shell_sort(self):
        start_time = time.time()
        array_copy = self.array.copy()
        step = len(array_copy) // 2

        while step > 0:

            for index in range(step, len(array_copy)):
                sort_ed = index

                while sort_ed >= step and array_copy[sort_ed - step] > array_copy[sort_ed]:
                    array_copy[sort_ed], array_copy[sort_ed - step] = array_copy[sort_ed - step], array_copy[sort_ed]
                    sort_ed -= step

            step //= 2

        return array_copy, (time.time() - start_time)

    def __fast_sort(self, array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return self.__fast_sort(less) + [pivot] + self.__fast_sort(greater)


    def fast_sort(self):
        start_time = time.time()
        array_copy = self.array.copy()
        return self.__fast_sort(array_copy), (time.time() - start_time)


    def __heapify(self, array, lenght, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < lenght and array[left] > array[root]:
            largest = left

        if right < lenght and array[right] > array[largest]:
            largest = right

        if largest != root:
            array[largest], array[root] = array[root], array[largest]
            self.__heapify(array, lenght, largest)


    def __heap_sort(self, array):
        lenght = len(array)

        for root in range(lenght, -1, -1):
            self.__heapify(array, lenght, root)

        for root in range(lenght - 1, 0, -1):
            array[root], array[0] = array[0], array[root]
            self.__heapify(array, root, 0)

        return array


    def heap_sort(self):
        start_time = time.time()
        array_copy = self.array.copy()
        return self.__heap_sort(array_copy), (time.time() - start_time)





"""
#Графики вычислений
array1000 = Sort([randint(1,100) for i in range(1,1000)])
ts1000 = array1000.selection_sort()[1]
ti1000 = array1000.insertion_sort()[1]
te1000 = array1000.exchange_sort()[1]
tsh1000 = array1000.shell_sort()[1]
tf1000 = array1000.fast_sort()[1]
th1000 = array1000.heap_sort()[1]
print("Вычисление 1000 - закончилось")




array5000 = Sort([randint(1,100) for i in range(1,5000)])
ts5000 = array5000.selection_sort()[1]
ti5000 = array5000.insertion_sort()[1]
te5000 = array5000.exchange_sort()[1]
tsh5000 = array5000.shell_sort()[1]
tf5000 = array5000.fast_sort()[1]
th5000 = array5000.heap_sort()[1]
print("Вычисление 5000 - закончилось")


array7500 = Sort([randint(1,100) for i in range(1,7500)])
ts7500 = array7500.selection_sort()[1]
ti7500 = array7500.insertion_sort()[1]
te7500 = array7500.exchange_sort()[1]
tsh7500 = array7500.shell_sort()[1]
tf7500 = array7500.fast_sort()[1]
th7500 = array7500.heap_sort()[1]
print("Вычисление 7500 - закончилось")


array10000 = Sort([randint(1,100) for i in range(1,10000)])
ts10000 = array10000.selection_sort()[1]
ti10000 = array10000.insertion_sort()[1]
te10000 = array10000.exchange_sort()[1]
tsh10000 = array10000.shell_sort()[1]
tf10000 = array10000.fast_sort()[1]
th10000 = array10000.heap_sort()[1]
print("Вычисление 10000 - закончилось")


plt.subplot(221)
plt.bar(["Selection","Insertion","Exchange","Shell","Fast","Heap"], [ts1000,ti1000,te1000,tsh1000,tf1000,th1000])
plt.ylabel("time, sec")
plt.xlabel("sorts")
plt.title("1000 elements")


plt.subplot(222)
plt.bar(["Selection","Insertion","Exchange","Shell","Fast","Heap"], [ts5000,ti5000,te5000,tsh5000,tf5000,th5000])
plt.ylabel("time, sec")
plt.xlabel("sorts")
plt.title("5000 elements")


plt.subplot(223)
plt.bar(["Selection","Insertion","Exchange","Shell","Fast","Heap"], [ts7500,ti7500,te7500,tsh7500,tf7500,th7500])
plt.ylabel("time, sec")
plt.xlabel("sorts")
plt.title("7500 elements")


plt.subplot(224)
plt.bar(["Selection","Insertion","Exchange","Shell","Fast","Heap"], [ts10000,ti10000,te10000,tsh10000,tf10000,th10000])
plt.ylabel("time, sec")
plt.xlabel("sorts")
plt.title("10000 elements")


plt.show()
"""

