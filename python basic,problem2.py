# write a method with fixed length of list 5. if user enter more then 5th value
#  in the list bottom value should be removed and new value should be added at the top of list
my_list = [1, 2, 3]

def add_to_list(value):
    if len(my_list) >= 5:
        my_list.pop()  
    my_list.insert(0, value) 

add_to_list(8)
add_to_list(66)
add_to_list(88)
add_to_list(4)
add_to_list(5)
# add_to_list(11)
# add_to_list(10)
print(my_list)  
