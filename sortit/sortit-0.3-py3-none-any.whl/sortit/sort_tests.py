from sortit import bubble_sort, selection_sort, insertion_sort, quick_sort

def run_sort_tests():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(alist)
    print(f"Bubble Sort result: {alist}.\nExpected: [17, 20, 26, 31, 44, 54, 55, 77, 93]\n")


    alist = [54,26,93,17,77,31,44,55,20]
    selection_sort(alist)
    print(f"Selection Sort result: {alist}.\nExpected: [17, 20, 26, 31, 44, 54, 55, 77, 93]\n")


    alist = [54,26,93,17,77,31,44,55,20]
    insertion_sort(alist)
    print(f"Insertion Sort result: {alist}.\nExpected: [17, 20, 26, 31, 44, 54, 55, 77, 93]\n")


    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist)
    print(f"Quick Sort result: {alist}.\nExpected: [17, 20, 26, 31, 44, 54, 55, 77, 93]\n")

if __name__ == "__main__":
    run_sort_tests()