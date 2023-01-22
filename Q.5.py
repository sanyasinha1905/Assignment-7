def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

def count_occurrences(arr, x):
    first_index = binary_search(arr, x)
    if first_index == -1:
        return 0
    last_index = first_index
    while last_index < len(arr) and arr[last_index] == x:
        last_index += 1
    return last_index - first_index

def main():
    arr = list(map(int, input("Enter an array of integers containing duplicates, separated by space: ").split()))
    arr.sort()
    x = int(input("Enter the element to search: "))
    index = binary_search(arr, x)
    if index != -1:
        print("Element found at index: ", index)
        print("Number of occurrences of the element: ", count_occurrences(arr, x))
    else:
        print("Element not found in the array.")

if __name__ == '__main__':
    main()
