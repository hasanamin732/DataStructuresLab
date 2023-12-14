class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.__insert_recursive(self.root, key)

    def __insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self.__insert_recursive(root.left, key)
        else:
            root.right = self.__insert_recursive(root.right, key)
        return root

    def delete(self, key):
        self.root = self.__delete_recursive(self.root, key)

    def __delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.__delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self.__delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.__min_value_node(root.right)
            root.key = temp.key
            root.right = self.__delete_recursive(root.right, temp.key)
        return root

    def search(self, key):
        return self.__search_recursive(self.root, key) is not None

    def __search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.__search_recursive(root.left, key)
        return self.__search_recursive(root.right, key)

    def sort(self):
        result = []
        self.__inorder_recursive(self.root, result)
        return result

    def __inorder_recursive(self, root, result):
        if root:
            self.__inorder_recursive(root.left, result)
            result.append(root.key)
            self.__inorder_recursive(root.right, result)

    def display(self):
        self.__display_recursive(self.root)

    def __display_recursive(self, root):
        if root:
            self.__display_recursive(root.left)
            print(root.key, end=' ')
            self.__display_recursive(root.right)

    def __min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


def main():
    bst = BST()
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Create a BST")
        print("2. Insert a new element")
        print("3. Delete an element")
        print("4. Search for an element")
        print("5. Sort the BST")
        print("6. Display the BST")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = list(map(int, input("Enter space-separated elements: ").split()))
            for elem in elements:
                bst.insert(elem)
            print("BST created.")

        elif choice == 2:
            key = int(input("Enter element to insert: "))
            bst.insert(key)
            print(f"{key} inserted.")

        elif choice == 3:
            key = int(input("Enter element to delete: "))
            if bst.search(key):
                bst.delete(key)
                print(f"{key} deleted.")
            else:
                print(f"{key} not found in BST.")

        elif choice == 4:
            key = int(input("Enter element to search: "))
            if bst.search(key):
                print(f"{key} found in BST.")
            else:
                print(f"{key} not found in BST.")

        elif choice == 5:
            sorted_elements = bst.sort()
            print("Sorted BST:", sorted_elements)

        elif choice == 6:
            print("BST elements:")
            bst.display()

        elif choice == 7:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
