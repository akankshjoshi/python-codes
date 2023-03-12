def sort_tuple(my_tup):

   my_len = len(my_tup)
   for i in range(0, my_len):

      for j in range(0, my_len-i-1):
         if (my_tup[j][-1] > my_tup[j + 1][-1]):
            temp = my_tup[j]
            my_tup[j]= my_tup[j + 1]
            my_tup[j + 1]= temp
   return my_tup

my_tuple =[(1, 92), (34, 25), (67, 89)]
print("The tuple is :")
print(my_tuple)

print("The sorted list of tuples are : ")
print(sort_tuple(my_tuple))