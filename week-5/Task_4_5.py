
#Task4
import timeit
print(timeit.timeit('sum([x for x in range(10000000)])',number=1))
print(timeit.timeit(stmt='np.arange(100000000).sum()',setup='import numpy as np',number=1))

#Task 5
import numpy as np

def median(list):
    array = np.sort(np.array(list))
    med = {}
    for i in range(array.shape[0]):
        if len(array[i]) % 2 == 0:
            med[f"row {i}"] = (array[i][len(array[i]) // 2] + array[i][len(array[i]) // 2 - 1]) / 2
        else:
            med[f"row {i}"] = array[i][len(array[i]) // 2]
    return med

def mode(arr):
    arr_flat = arr.flatten()  # Flatten the array to a 1D array
    unique_values = np.unique(arr_flat)
    modes = []
    max_count = 0

    for value in unique_values:
        count = np.count_nonzero(arr_flat == value)
        if count > max_count:
            max_count = count
            modes = [value]
        elif count == max_count:
            modes.append(value)

    if len(modes) == len(arr_flat):
        return None
    else:
        return modes
        

print(median(np.array([[20,23,24],[1,7,4],[455,9,86]])))
print(mode(np.array([[20,23,24],[1,7,4],[455,24,86]])))