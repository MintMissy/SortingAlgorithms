from array_generator import random_int_array
from sorting_algorithms import *
from matplotlib import pyplot as plt


def save_results_to_file(results, file_name):
    """
    This function saves times needed to sorting array by algorithm to file in results folder

    :param results: Dictionary storing sorting times for array's length
    :type results: dict
    :param file_name: Name of the file where data is going to be stored
    :type file_name: str
    """
    with open(f"results/{file_name}.txt", "w") as f:
        for result in results:
            f.write(f"{result},{results[result]}\n")


def draw_efficiency_graph(*data):
    """
    This function draws a efficiency graph of sorting algorithms

    :param data: list with dictionary(list length: sorted time), string(algorithm label) and string(hex color)
    :type data: list
    """
    # Set background color outside graph
    plt.figure(facecolor='#282c34')
    # Set background color inside graph
    ax = plt.gca()
    ax.set_facecolor('#282c34')
    # Change axles color
    ax.spines['bottom'].set_color('#4e5b6d')
    ax.spines['top'].set_color('#4e5b6d')
    ax.spines['right'].set_color('#4e5b6d')
    ax.spines['left'].set_color('#4e5b6d')
    # Change values at axles color
    ax.tick_params(axis='x', colors='#4e5b6d')
    ax.tick_params(axis='y', colors='#4e5b6d')
    # Enable graph grid
    plt.grid(True, color='#4e5b6d')

    # Create graph title
    plt.title('Sorting efficiency', fontsize=30, color='#d55fde')
    # Create names x and y label
    plt.xlabel('List length', fontsize=15, color='#3477d8')
    plt.ylabel('Sorting Time (s)', fontsize=15, color='#3477d8')

    # Loop through data passed in parameters to draw algorithm efficiency
    for information in data:
        plt.plot(*zip(*information[0].items()), label=information[1], color=information[2])

    # Add legend with gray bg color, blue label text and 0% opacity
    plt.legend(facecolor='#4e5b6d', edgecolor='#4e5b6d', labelcolor='#5294f2', framealpha=1)

    # Show graph to user
    plt.show()


# This list store amount of numbers to generate in array
numbers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
min_generated_number = -100
max_generated_number = 100

# These dictionaries store sorting times for array's length
results_bubble_sort = {}
results_optimized_bubble_sort = {}
results_selection_sort = {}

for number in numbers:
    # Create random int array to test sorting
    array_to_sort = random_int_array(min_generated_number, max_generated_number, number)

    # Calculate sorting time and save it to dictionary result
    results_bubble_sort[number] = test_algorithm(bubble_sort, array_to_sort)
    results_optimized_bubble_sort[number] = test_algorithm(optimized_bubble_sort, array_to_sort)
    results_selection_sort[number] = test_algorithm(selection_sort, array_to_sort)
    print(f"{number} passed!")

# Save results to files
save_results_to_file(results_bubble_sort, 'bubble_sorting_times')
save_results_to_file(results_optimized_bubble_sort, 'optimized_bubble_sorting_times')
save_results_to_file(results_selection_sort, 'selection_sorting_times')

draw_efficiency_graph(
    [results_bubble_sort, "Bubble Sort", '#5ce1d1'],
    [results_optimized_bubble_sort, "Optimized Bubble Sort", '#e1cf5c'],
    [results_selection_sort, "Selection Sort", '#81e15c'])
