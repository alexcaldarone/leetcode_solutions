import random

def selection_sort(x: list[int]) -> None:
    for i in range(len(x)):
        min_idx = i
        for j in range(i, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]

def insertion_sort(x: list[int]):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]
        while j >= 0 and x[j] > key:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key

def bubble_sort(x: list[int]):
    if len(x) <= 1:
        return x
    
    for i in range(len(x)-1, 0, -1):
        swapped = False
        for j in range(0, i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                swapped = True
        if swapped == False:
            break

def merge_sort(x: list[int]):
    def _merge(l, r):
        i, j = 0, 0
        res = []
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        # final checks
        while i < len(l):
            res.append(l[i])
            i += 1
        while j < len(r):
            res.append(r[j])
            j += 1
        return res
    
    if len(x) == 0:
        return []
    if len(x) == 1:
        return x

    m = len(x) // 2
    l = merge_sort(x[:m])
    r = merge_sort(x[m:])
    return _merge(l, r)

def quick_sort(x: list[int], low, high=None):
    def _partition(arr, l, h):
        piv = random.randint(l, h)
        arr[piv], arr[h] = arr[h], arr[piv]
        piv = arr[h]
        i = l-1
        for j in range(l, h):
            if arr[j] <= piv:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[h] = arr[h], arr[i+1] 
        return i+1
    
    if high is None:
        high = len(x)-1
    if low >= high:
        return
    
    if low < high:
        p = _partition(x, low, high)
        quick_sort(x, low, p-1)
        quick_sort(x, p+1, high)

def test_sorting_algorithm(sort_func, **kwargs):
    """
    sort_func: a function that takes a list and returns a sorted list.
               It should not modify the input list unless that's intended.
    """
    test_cases = [
        [],  # empty array
        [1],  # single element
        [2, 1],  # two elements, unsorted
        [1, 2, 3, 4, 5],  # already sorted
        [5, 4, 3, 2, 1],  # reverse sorted
        [3, 1, 4, 1, 5],  # random small
        [10, -1, 2, 9, 0],  # mixed positive and negative
        [2, 3, 2, 1, 1],  # duplicates
        [5, 5, 5, 5],  # all same element
        [-3, -1, -4, 2, 0],  # mixed negatives and positives
        [0, -2, 5, -1, 3],  # mixed negatives and positives
        list(range(1000, 0, -1)),  # large reverse sorted
        [0, 1, 0, 1, 0, 1],  # repeating pattern
        [1, 2, 1, 2, 1, 2],  # repeating pattern
    ]

    for i, case in enumerate(test_cases, 1):
        # Copy to avoid modifying the original in case of in-place sort
        input_copy = case.copy()
        result = sort_func(input_copy, **kwargs)
        
        # inplace sort
        if result is None:
            result = input_copy

        expected = sorted(case)
        if result == expected:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print(f"  Input:    {case}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")

if __name__ == "__main__":
    print("--- SELECTION SORT ---")
    test_sorting_algorithm(selection_sort)
    print("--- INSERTION SORT ---")
    test_sorting_algorithm(insertion_sort)
    print("--- BUBBLE SORT ---")
    test_sorting_algorithm(bubble_sort)
    print("--- MERGE SORT ---")
    test_sorting_algorithm(merge_sort)
    print("--- QUICKSORT ---")
    test_sorting_algorithm(quick_sort, low=0)