from SinglyLinkedList import SLL

sll=SLL("abc")

sll.append("abc")
sll.append("abc")
sll.append("aec")
sll.append("axc")
sll.append("ahc")
sll.append(50)
sll.append(50)
sll.append(50)
sll.append(50)
sll.append(234)
sll.insert(0,53)
sll.insert(3,53)
sll.insert(2,100)

print(f"Linked List: {sll}   Count of 50: {sll.count50s()}")

sll.unique()
print(f"Duplicates removed: {sll}")

sll.groupOddEvens()
print(f"OddEvens Grouped: {sll}")

sll.remove("axc")
print(f'Removed "axc" from my SLL: {sll}')

sll.pop(0)
print(f'Popped the node at 0th index from my SLL: {sll}')

mysll2=SLL()
mysll2=sll.removeEvens()
print(f"Odd Nodes:{sll} Even Nodes: {mysll2}")

mysll2.destroy()
print(f"Destroyed My Even Nodes SLL:{mysll2}")