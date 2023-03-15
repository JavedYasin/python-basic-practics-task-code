# write a method in python  with take key, value from the user and add that value in the list..
#  if key is already filled should return message to user to chose another key. length of 
#  list will be 10


my_dict = {}

def add_key_value(key, val):
    if len(my_dict) >= 10:
        print("List is already full")
    elif key in my_dict:
        print("Key is already taken. Try another one.")
    else:
        my_dict[key] = val
        print("Added key-value pair:", key, val)


add_key_value(1, 'Mudassar')
add_key_value(2, 'Javed')
add_key_value(1, 'Mohsin')
print(my_dict)

