def find_min(lst):
    if not lst:
        return None

    min_element = lst[0]
    for num in lst:
        if num < min_element:
            min_element = num

    return min_element
my_list = [5, 3, 8, 2, 7]
min_element = find_min(my_list)
print("Мінімальний елемент списку:", min_element)