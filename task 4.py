def delete_number(list, number):

   count = 0

   for i in list:

       if i == number:

           list.remove(i)

           count += 1

   return count
