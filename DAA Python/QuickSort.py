import random

def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)

def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i += 1
        while (i <= j and alist[j] >= pivot):
            j -= 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

try:
    size = int(input('Enter the number of random numbers to generate: '))
    if size <= 0:
        raise ValueError("Size must be a positive integer.")

    alist = [random.randint(0, 10000) for _ in range(size)]

    print('Unsorted list:', alist) 
    quicksort(alist, 0, len(alist))
    print('Sorted list:', alist)

except ValueError as e:
    print(f'Invalid input: {e}')
