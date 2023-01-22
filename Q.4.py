def merge_sort(marks):
    if len(marks) <= 1:
        return marks
    mid = len(marks) // 2
    left = marks[:mid]
    right = marks[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def main():
    n = int(input("Enter the number of students: "))
    marks = []
    for i in range(n):
        mark = int(input("Enter the mark for student {}: ".format(i+1)))
        marks.append(mark)
    print("Original List: ", marks)
    sorted_marks = merge_sort(marks)
    print("Sorted List: ", sorted_marks)

if __name__ == '__main__':
    main()
