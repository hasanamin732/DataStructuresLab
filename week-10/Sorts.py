import matplotlib.pyplot as plt
import numpy as np
import timeit

def selection(mylist):
    n=len(mylist)
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if mylist[j]<mylist[min]:
                min=j
        mylist[i],mylist[min]=mylist[min],mylist[i]
    return mylist



def insertion(mylist):
    n=len(mylist)
    for i in range(1,n):
        key=mylist[i]
        j=i-1

        while j>=0 and mylist[j]>key:
            mylist[j+1]=mylist[j]
            j-=1
        mylist[j+1]=key
    return mylist

def bubble(mylist):
    n=len(mylist)
    for i in range(n-1):
        flag=False
        for j in range(n-i-1):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                flag=True
        if not flag:
            return mylist
    return mylist

def time_sorting_algorithm(algorithm, arr):
    # setup_code = f"from __main__ import {algorithm}, arr"
    setup_code=f"import numpy as np; from __main__ import {algorithm}"
    stmt = f"{algorithm}({list(arr)})"
    # print(stmt)
    execution_time = timeit.timeit(stmt, setup=setup_code, number=int(np.log10(len(list(arr)))))
    return execution_time


rng = np.random.default_rng()

# Arrays to test (using np.random.uniform for floats)
arr1 = rng.uniform(low=0.0, high=1000.0, size=100)
arr2 = rng.uniform(low=0.0, high=1000.0, size=1000)
arr3 = rng.uniform(low=0.0, high=1000.0, size=5000)
# List of sorting algorithms
sorting_algorithms = ["selection","insertion","bubble"]



###############################



def run_trials(algorithms, arrays, num_trials):
    results = {alg: {len(arr): [] for arr in arrays} for alg in algorithms}

    for _ in range(num_trials):
        for arr in arrays:
            for algorithm in algorithms:
                time_taken = time_sorting_algorithm(algorithm, arr)
                results[algorithm][len(arr)].append(time_taken)

    avg_results = {alg: {size: np.mean(times) for size, times in data.items()} for alg, data in results.items()}
    return avg_results

# Number of trials to run
num_trials = 5

# Run trials for sorting algorithms on arrays and get average times
average_results = run_trials(sorting_algorithms, [arr1, arr2, arr3], num_trials)
ascending_average_results=run_trials(sorting_algorithms, [np.sort(arr1),np.sort(arr2),np.sort(arr3)],num_trials)
descending_average_results=run_trials(sorting_algorithms, [np.sort(arr1)[::-1],np.sort(arr2)[::-1],np.sort(arr3)[::-1]],num_trials)
# Plotting average results

num_scenarios = 3  # For Average, Ascending, Descending
fig, axs = plt.subplots(num_scenarios, 1, figsize=(10, 8*num_scenarios))

scenarios = ['Average', 'Ascending', 'Descending']

for i, scenario in enumerate(scenarios):
    for algorithm in sorting_algorithms:
        sizes = []
        avg_times = []
        if scenario == 'Average':
            data = average_results[algorithm]
        elif scenario == 'Ascending':
            data = ascending_average_results[algorithm]
        else:
            data = descending_average_results[algorithm]
        
        sizes = list(data.keys())
        avg_times = list(data.values())

        axs[i].plot(sizes, avg_times, marker='o', label=f"{algorithm}")

    axs[i].set_xlabel('Sizes')
    axs[i].set_ylabel('Average Times')
    axs[i].set_title(f'Comparison for {scenario} Scenarios')
    axs[i].legend()

plt.tight_layout()
plt.show()
