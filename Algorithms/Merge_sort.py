def merge(arr1, low, m, n):
    i=k= low
    j = m+1
    c = []
    print("done 1")
    while i <= m and j <= n:
        if arr1[i] < arr1[j]:
            c.append( arr1[i])
            i = i + 1
            k = k + 1
        else :
            c.append(arr1[j])
            j = j + 1
            k = k + 1
    while i <= m:
        c.append(arr1[i])
        i = i + 1
        k = k + 1
    while j <= n:
        c.append(arr1[j])
        j = j + 1
        k = k + 1
    arr1 = c
    print(c)


def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr,low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def main():
    ast = [23,12,54,2,53,21,78]
    print(ast)
    merge_sort(ast, 0, 6)
    print(ast)


main()
