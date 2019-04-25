def partition(arr, low, high):
    pivot = arr[low]
    i = low; j = high
    while i < j :
        while arr[i] <= pivot and i < j:
            i = i + 1
        while arr[j] > pivot and i <= j:
            j = j - 1
        if i < j:
            swap_list(arr, i, j)
    swap_list(arr, low, j)
    return j


def quick_sort(arr, low, high):
    if low < high :
        j = partition(arr, low, high)
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)


def swap_list(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def main():
    mdf = [34,7,2,43,78,23,65]
    print(mdf)
    quick_sort(mdf, 0, 7-1)
    print(mdf)


main()   
