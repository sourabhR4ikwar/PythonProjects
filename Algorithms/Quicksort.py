def partition_array(arr, low, high):
    pivot = arr[low]
    i = low; j = high
    while i < j:
        print(i, j)
        print("check 1")
        while arr[i] <= pivot and i < j:
            print("check 2")
            i = i + 1

        while arr[j] > pivot and i <= j:
            print("check 3")
            j = j - 1

        print(i,j)
        if i < j:
            print("check 4")
            swap_list(arr, i, j)
    swap_list(arr, low, j)
    return j


def quick_sort(arr, low, high):
    print("check 5")
    if low < high:
        j = partition_array(arr, low, high)
        print(arr)
        print("check 7")
        quick_sort(arr, low, j-1)
        print("check 6")
        quick_sort(arr, j+1, high)


def swap_list(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def main():
    ast = [23, 36, 12, 78, 1, 3, 65]
    print(ast)
    quick_sort(ast, 0, 6)
    print(ast)

main()
