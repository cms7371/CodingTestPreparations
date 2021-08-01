def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def quick_sort(arr, start, end):
    # 마지막을 pivot으로
    current = start
    for i in range(start, end + 1):
        if arr[i] < arr[end]:
            arr[i], arr[current] = arr[current], arr[i]
            current += 1
    arr[current], arr[end] = arr[end], arr[current]
    if current - start > 1:
        quick_sort(arr, start, current - 1)
    if end - current > 1:
        quick_sort(arr, current + 1, end)




a = [3, 2, 9, 7, 6, 5, 1, 4, 8]


