import random


def random_int_array(min_number, max_number, length):
    """
    Create array with random number from given range

    :param min_number: Minimum value of number in the array
    :type min_number: int
    :param max_number: Maximum value of number in the array
    :type max_number: int
    :param length: Numbers to generate in the array
    :type length: int
    :return: Array with randomly generated numbers
    """
    array = []
    while len(array) < length:
        array.append(random.randint(min_number, max_number))
    return array
