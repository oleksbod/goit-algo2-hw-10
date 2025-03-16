import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Детермінований QuickSort (опорний елемент - останній)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  # останній елемент
        less = [x for x in arr[:-1] if x <= pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        return deterministic_quick_sort(less) + [pivot] + deterministic_quick_sort(greater)

# Рандомізований QuickSort (опорний елемент - випадковий)
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        less = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        greater = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
        return randomized_quick_sort(less) + [pivot] + randomized_quick_sort(greater)

# Функція вимірювання середнього часу виконання
def measure_time(sort_function, array, repeats=5):
    times = []
    for _ in range(repeats):
        arr_copy = array.copy()
        start_time = time.perf_counter()
        sort_function(arr_copy)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return sum(times) / repeats

def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    random_quick_times = []
    deterministic_quick_times = []

    for size in sizes:
        print(f"Розмір масиву: {size}")
        test_array = [random.randint(0, 1_000_000) for _ in range(size)]

        rand_time = measure_time(randomized_quick_sort, test_array)
        det_time = measure_time(deterministic_quick_sort, test_array)

        random_quick_times.append(rand_time)
        deterministic_quick_times.append(det_time)

        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд\n")

    # Вивід таблиці
    print(f"{'Розмір':>10} | {'Рандомізований (с)':>20} | {'Детермінований (с)':>20}")
    print("-" * 60)
    for i in range(len(sizes)):
        print(f"{sizes[i]:>10} | {random_quick_times[i]:>20.4f} | {deterministic_quick_times[i]:>20.4f}")

    # Побудова графіку
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, random_quick_times, marker='o', label='Рандомізований QuickSort')
    plt.plot(sizes, deterministic_quick_times, marker='s', label='Детермінований QuickSort')
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
