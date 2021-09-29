import time


def test_algorithm(sorting_algorithm, array):
    """
    This function test sorting algorithms on int arrays

    :param sorting_algorithm: Algorithm that will sort the array
    :type sorting_algorithm: fun
    :param array: Array to sort
    :type array: list
    :return: Time after array is sorted
    """
    # Initialize variable storing starting time of sorting
    start = time.time()
    sorting_algorithm(array.copy())
    # Calculate sorting time then return it
    return time.time() - start


def bubble_sort(array):
    """
    This function sorts array with bubble sort

    :param array: Array to sort
    :type array: list
    :return: Sorted array
    """
    # Variable that is used to optimize algorithm
    for i in range(len(array)):
        for j in range(len(array) - 1):
            # Swap elements in array
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def optimized_bubble_sort(array):
    """
    This function sorts array with optimized bubble sort

    :param array: Array to sort
    :type array: list
    :return: Sorted array
    """
    # Variable that is used to optimize algorithm
    swapped = False
    for i in range(len(array)):
        for j in range(len(array) - 1):
            # Swap elements in array
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break
    return array


def selection_sort(array):
    """
    This function sorts array with selection sort

    :param array: Array to sort
    :type array: list
    :return: Sorted array
    """
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[minimum] > array[j]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array


def insertion_sort(array):
    """
    This function sorts array with insertion sort

    :param array: Array to sort
    :type array: list
    :return: Sorted array
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
