def multiply_list_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result
my_list = [2, 3, 4, 5]
result = multiply_list_elements(my_list)
print("Добуток елементів списку:", result)
