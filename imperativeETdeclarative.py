# user defined Sorting function in ascending order
def bestz_sort(arr):
    for n in range(len(arr)):
        for m in range(n+1, len(arr)):
            if arr[n] > arr[m]:
                arr[n], arr[m] = arr[m], arr[n]
    return arr


if __name__=='__main__':
    lst = [4, 5, 2, 1, 3, 10, 6, 9, 7, 8]

    print(f"Imperative Programming: {bestz_sort(lst)}")


    print(f"Declarative Programming: {sorted(lst)}") 