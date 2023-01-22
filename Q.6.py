def remove_duplicates(arr):
    return list(set(arr))

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    arr = list(map(int, input("Enter a list of integers, separated by space: ").split()))
    arr = remove_duplicates(arr)
    print("List after removing duplicates: ", arr)
    print("List after sorting using selection sort: ", selection_sort(arr))
    print("List after sorting using bubble sort: ", bubble_sort(arr))

if __name__ == '__main__':
    main()
