# write a method which can create a multi die-mention array by getting number of 
# values of first list and number of values for the associative list, display the 
# list as value in table formate

def create_multi_dimensional_array():
    # get number of values for the first list
    n = int(input("Enter number of values for the first list: "))

    # get number of values for the associative list
    m = int(input("Enter number of values for the associative list: "))

    # create multi-dimensional array
    arr = [[0 for i in range(m)] for j in range(n)]

    # populate the array
    for i in range(n):
        for j in range(m):
            arr[i][j] = input("Enter value for index ({},{}) of the array: ".format(i, j))

    # display the array as a table
    print("Multi-dimensional array:")
    for row in arr:
        for val in row:
            print("{:<10}".format(val), end="")
        print()










