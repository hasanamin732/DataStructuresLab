import Array
# maxSize = 10                    # Max size of the array
# arr = Array.Array(maxSize)      # Create an array object
   
# arr.insertAtEnd(77)                  # Insert 10 items
# arr.insertAtEnd(99)
# arr.insertAtEnd("foo")
# arr.insertAtEnd("bar")
# arr.insertAtEnd(44)
# arr.insertAtEnd(55)
# arr.insertAtEnd(12.34)
# arr.insertAtEnd(0)
# arr.insertAtEnd("baz")
# #arr.insertAtEnd(-17)


# print("Array containing", len(arr), "items")
# arr.traverse()

# print("Search for 12 returns", arr.search(12))

# print("Search for 12.34 returns", arr.search(12.34))

# print("Deleting 0 returns", arr.delete(0))
# print("Deleting 17 returns", arr.delete(17))

# print("Setting item at index 3 to 33")
# arr.insertAtPosition(3, 33)
# #arr.insertAtPosition(5, 61)
# #arr.insertAtPosition(6, 42)

# print("Array after deletions has", len(arr), "items")
# arr.traverse()

#1b
arr2=Array.Array(6)
arr2.insertAtEnd(77)                 
arr2.insertAtEnd(99)
arr2.insertAtEnd("foo")
arr2.insertAtEnd("foo")
arr2.insertAtEnd(77)
arr2.insertAtEnd(0)
arr3=Array.Array(0)
print("Removing maximum number from an array which has max=99")
print(f"{arr2.deleteMaxNum()}")
print("Removing maximum number from an empty array")
print(f"{arr3.deleteMaxNum()}")
# works fine

#Task 2
print("Array before duplicate removal")
arr2.traverse()
arr2.removeDupes()

print("Array after duplicate removal")
arr2.traverse()