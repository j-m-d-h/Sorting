# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    l = 0
    r = 0
    for i in range(elements):
        if l >= len(arrA):
            merged_arr[i] = arrB[r]
            r += 1
        elif r >= len(arrB):
            merged_arr[i] = arrA[l]
            l += 1
        elif arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
        else:
            merged_arr[i] = arrB[r]
            r += 1
    return merged_arr

print(merge([6,7,8,9,0,11], [2,3,4,5,10]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    left_arr = arr[:(len(arr)//2)]
    right_arr = arr[(len(arr)//2):]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return merge(left_arr, right_arr)

a = [4,7,5,9,8,2,1,3,0]
print(merge_sort(a))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
