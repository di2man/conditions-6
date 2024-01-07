def power_list(lst, power):

 result = []

 for x in lst:

   result.append(x**power)

 return result

nums = [1, 2, 3, 4]

powered = power_list(nums, 3)

print(powered) # [1, 8, 27, 64]

