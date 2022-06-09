def find_pair(lst, target):
    sorted_lst = sorted(lst)
    left = 0
    right = len(sorted_lst)-1

    while left < right:
        if sorted_lst[left] + sorted_lst[right] == target:
            return (sorted_lst[left], sorted_lst[right])
        
        if sorted_lst[left] + sorted_lst[right] < target:
            left = left + 1
        else:
            right = right - 1

    return ('No pairs sum to the target')

my_list=  [ 3, 7, 6, 8]
print(find_pair(my_list, 9))