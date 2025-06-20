# Встроенные методы Python
# Сортировка на месте
    nums = [54, 43, 3, 11, 0]
    nums.sort()
    print(nums)  # [0, 3, 11, 43, 54]

# Сортировка с созданием нового списка
    nums2 = [54, 43, 3, 11, 0]
    sorted_nums = sorted(nums2)
    print(sorted_nums)  # [0, 3, 11, 43, 54]

# Обратная сортировка
    nums.sort(reverse=True)
    print(nums)  # [54, 43, 11, 3, 0]

# Классические алгоритмы сортировки
# 1. Пузырьковая сортировка (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2. Сортировка выбором (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

# 3. Сортировка вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 4. Сортировка слиянием (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# 5. Быстрая сортировка (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 6. Пирамидальная сортировка (Heap Sort)
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# 7. Сортировка перемешиванием (шейкерная, Cocktail Sort)
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr

# Использование ключей сортировки
# Сортировка по длине строки
    words = ['cat', 'elephant', 'dog', 'mouse']
    words.sort(key=len)
    print(words)  # ['cat', 'dog', 'mouse', 'elephant']

# Сортировка по последнему символу строки
    words.sort(key=lambda x: x[-1])
    print(words)

# Comb Sort (Сортировка расчёской)
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
            i += 1
    return arr

# Пример использования
data = [34, 2, 78, 1, 45, 99, 23]
print(comb_sort(data))  # [1, 2, 23, 34, 45, 78, 99]

# Counting Sort (Сортировка подсчётом)
def counting_sort(array):
    size = len(array)
    output = [0] * size
    count = [0] * (max(array) + 1)

    for i in range(size):
        count[array[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]

# Пример использования
data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)
print(data)  # [1, 2, 2, 3, 3, 4, 8]

# Radix Sort (Поразрядная сортировка)
def radix_sort(myArray):
    maxVal = max(myArray)
    exp = 1
    while maxVal // exp > 0:
        buckets = [[] for _ in range(10)]
        for val in myArray:
            radixIndex = (val // exp) % 10
            buckets[radixIndex].append(val)
        myArray = [val for bucket in buckets for val in bucket]
        exp *= 10
    return myArray

# Пример использования
data = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(data))  # [2, 24, 45, 66, 75, 90, 170, 802]

# Shell Sort (Сортировка Шелла)
def shell_sort(array):
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2

# Пример использования
data = [9, 8, 3, 7, 5, 6, 4, 1]
shell_sort(data)
print(data)  # [1, 3, 4, 5, 6, 7, 8, 9]

# Binary Insertion Sort (Сортировка вставками с двоичным поиском)
def binary_search(alist, key, start, end):
    if end - start <= 1:
        if key < alist[start]:
            return start - 1
        else:
            return start
    mid = (start + end) // 2
    if alist[mid] < key:
        return binary_search(alist, key, mid, end)
    elif alist[mid] > key:
        return binary_search(alist, key, start, mid)
    else:
        return mid

def binary_insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        pos = binary_search(alist, temp, 0, i) + 1
        for k in range(i, pos, -1):
            alist[k] = alist[k - 1]
        alist[pos] = temp

# Пример использования
data = [37, 23, 0, 17, 12, 72, 31]
binary_insertion_sort(data)
print(data)  # [0, 12, 17, 23, 31, 37, 72]

# Timsort — гибридная сортировка, используемая по умолчанию в Python.
# Она сочетает сортировку слиянием и сортировку вставками, оптимизирована для реальных данных.
# Используйтся `sorted()` или `list.sort()`.