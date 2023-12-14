class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(arr):
    if not arr:
        return None

    nodes = [None if val == 'n' else Node(val) for val in arr]
    root = nodes[0]

    for i in range(len(arr)):
        if nodes[i]:
            left_index = 2 * i + 1 # left ndex at 2n+1 position and right at 2n+2
            right_index = 2 * i + 2

            if left_index < len(arr):
                nodes[i].left = nodes[left_index]
            if right_index < len(arr):
                nodes[i].right = nodes[right_index]

            if i != 0 and not nodes[(i - 1) // 2]:
                raise ValueError("Tree cannot be built")

    return root

def print_tree(root):
    if not root:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val, end=" ")
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("n", end=" ")
    print()

# Test cases
test_cases = [
    [],
    ['n', 'n', 'n'],
    [55, 12, 71],
    [55, 12, 'n', 4],
    [55, 12, 'n', 4, 'n', 'n', 'n', 'n', 8, 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 6, 'n'],
    [55, 12, 'n', 'n', 'n', 'n', 4, 'n', 8, 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 6, 'n']
]

for arr in test_cases:
    try:
        tree_root = build_tree(arr)
        print_tree(tree_root)
    except ValueError as e:
        print(e)
