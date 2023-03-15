# write a method with list of random numbers, when user add new value methode will 
# check if the value already exist in list return message "value already in the list
# other wise add the value in the list and display back the list till that value

my_list = [1,3,52, 53, 829, 728]

def check_value(val):
    if val in my_list:
        print("The value is already exist in the list")
    else:
        my_list.append(val)
        print(f"The value {val} add successfully")
        print(my_list)

check_value(5)
check_value(66)
check_value(53)
check_value(54)