# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for n in range(cur_index+1, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



    return arr

my_list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 25, 33, 19, 62, 42, 28, 3, 5]

#print(selection_sort(my_list))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    counter = len(arr)-1
    while counter > 0:
        counter = len(arr)-1
        for i in range(0, len(arr)-1):
            h = i+1
            if arr[i] > arr[h]:
                arr[i], arr[h] = arr[h], arr[i]
            else:
                counter -= 1
        print(counter)
    return arr

print(bubble_sort(my_list))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
