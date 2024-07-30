import time
import random
import matplotlib.pyplot as plt
from red_black_tree import RedBlackTree

def measure_performance(tree_class, sizes):
    results = {}
    for size in sizes:
        data = [random.randint(0, 1000000) for _ in range(size)]
        start_time = time.time()

        tree = tree_class()
        for value in data:
            tree.insert(value)

        insertion_time = time.time() - start_time

        start_time = time.time()
        for value in data:
            tree.search(value)

        search_time = time.time() - start_time

        results[size] = {
            'insertion_time': insertion_time,
            'search_time': search_time
        }

    return results

def plot_performance(results, title):
    sizes = list(results.keys())
    insertion_times = [results[size]['insertion_time'] for size in sizes]
    search_times = [results[size]['search_time'] for size in sizes]

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, insertion_times, label='Insertion Time')
    plt.plot(sizes, search_times, label='Search Time')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    sizes = [100, 1000, 10000, 100000]
    rb_tree_results = measure_performance(RedBlackTree, sizes)
    plot_performance(rb_tree_results, 'Red-Black Tree Performance')
