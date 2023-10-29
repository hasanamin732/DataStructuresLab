import timeit
import numpy as np
from Array import Array
import matplotlib.pyplot as plt

# Define the code blocks to be timed
code_list = """
mylist=[2,2,4,3,5,6,4,5,8]
mylist.remove(max(mylist))
mylist=list(set(mylist))
"""

code_numpy = """
numpyArr=np.array([2,2,4,3,5,6,4,5,8])
indices=np.where(numpyArr==numpyArr.max())
newarr=np.delete(numpyArr,indices)
newarr=np.unique(newarr)
"""

code_custom_array = """
mylist=[2,2,4,3,5,6,4,5,8]
myarr=Array(len(mylist))
for i in mylist:
    myarr.insertAtEnd(i)
myarr.deleteMaxNum()
myarr.removeDupes()
"""

code_list2 = """
mylist=[2,2,4,3,5,6,4,5,8,20,30,76,45,66,66,21,34]
mylist.remove(max(mylist))
mylist=list(set(mylist))
"""

code_numpy2 = """
numpyArr=np.array([2,2,4,3,5,6,4,5,8,20,30,76,45,66,66,21,34])
indices=np.where(numpyArr==numpyArr.max())
newarr=np.delete(numpyArr,indices)
newarr=np.unique(newarr)
"""

code_custom_array2 = """
mylist=[2,2,4,3,5,6,4,5,8,20,30,76,45,66,66,21,34]
myarr=Array(len(mylist))
for i in mylist:
    myarr.insertAtEnd(i)
myarr.deleteMaxNum()
myarr.removeDupes()
"""

# Set up the number of repetitions
repeats = 10000

# Time each block for the first set of data
time_list = timeit.timeit(stmt=code_list, number=repeats, globals=globals())
time_numpy = timeit.timeit(stmt=code_numpy, number=repeats, globals=globals())
time_custom_array = timeit.timeit(stmt=code_custom_array, number=repeats, globals=globals())

# Time each block for the second set of data
time_list2 = timeit.timeit(stmt=code_list2, number=repeats, globals=globals())
time_numpy2 = timeit.timeit(stmt=code_numpy2, number=repeats, globals=globals())
time_custom_array2 = timeit.timeit(stmt=code_custom_array2, number=repeats, globals=globals())

# Create subplots to visualize the timing results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

blocks = ['List', 'NumPy Array', 'Custom Array']
times = [time_list, time_numpy, time_custom_array]

axes[0].bar(blocks, times)
axes[0].set_xlabel('Code Block')
axes[0].set_ylabel('Execution Time (seconds)')
axes[0].set_title('Set 1')

blocks2 = ['List', 'NumPy Array', 'Custom Array']
times2 = [time_list2, time_numpy2, time_custom_array2]

axes[1].bar(blocks2, times2,color=['red'])
axes[1].set_xlabel('Code Block')
axes[1].set_ylabel('Execution Time (seconds)')
axes[1].set_title('Set 2')

plt.tight_layout()
plt.show()
