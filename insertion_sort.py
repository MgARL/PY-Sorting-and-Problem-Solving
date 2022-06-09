def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]

        while i > 0 and lst[i - 1] > current_value:
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current_value
    
    return lst

sample_list = [5, 8, 1, 22, 18, 6, 2]
print(f"Unsorted list: {sample_list}")
insertion_sort(sample_list)
print(f"Sorted list: {sample_list}")