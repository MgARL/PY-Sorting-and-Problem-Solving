def selection_sort(lst):
    for i in range(0, len(lst) - 1 ):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[i], lst[min] = lst[min], lst[i]
    return lst

sample_list = [5, 8, 1, 22, 18, 6, 2]
print(f"Unsorted list: {sample_list}")
selection_sort(sample_list)
print(f"Sorted list: {sample_list}")