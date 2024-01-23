# Быстрая сортировка O(n log n) если опорный элемент выбирается случайно
def quicksort(arr):
    if len(arr) < 2:       # если массив пустой или состоит из 1 элемента
        return arr         # то возвращаем такой массив
    else:
        pivot = arr[0]     # опорный элемент
        less = [i for i in arr[1:] if i < pivot]     # массив эл меньше опорного
        greater = [i for i in arr[1:] if i > pivot]  # массив эл больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)  # Сортируем Массивы с помощью Рекурсии