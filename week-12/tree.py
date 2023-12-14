class Tree:
    def __init__(self, datum, Lchild=None, Rchild=None):
        self.Lchild = Lchild
        self.Rchild = Rchild
        self.datum = datum

    def height(self):
        if self is None:
            return 0

        left_height = self.Lchild.height() if self.Lchild else 0
        right_height = self.Rchild.height() if self.Rchild else 0

        return 1 + max(left_height, right_height)

    def tree_size(self, node=True):
        if node is True: node = self
        if node is None:
            return 0
        return 1 + self.tree_size(node.Lchild) + self.tree_size(node.Rchild)

    def add_item(self, item):
        if self is None:
            self = Tree(item)
        elif self.Lchild is None:
            self.Lchild = Tree(item)
        elif self.Rchild is None:
            self.Rchild = Tree(item)
        else:
            right = self.Rchild.tree_size()
            left = self.Lchild.tree_size()
            if left <= right:
                self.Lchild.add_item(item)
            else:
                self.Rchild.add_item(item)

    def post_order_traversal(self):
        result = []
        if self:
            if self.Lchild:
                result.extend(self.Lchild.post_order_traversal())
                # print(result, "l")
            if self.Rchild:
                result.extend(self.Rchild.post_order_traversal())
                # print(result, "r")
            result.append(
                self.datum
            )  # left node --> right node --> root node recursion
        return result

    def pre_order_traversal(self):
        result = []
        if self:
            result.append(
                self.datum
            )  # root node --> left node --> right node recursion
            if self.Lchild:
                result.extend(self.Lchild.pre_order_traversal())
                # print(result, "l")
            if self.Rchild:
                result.extend(self.Rchild.pre_order_traversal())
                # print(result, "r")
        return result

    def in_order_traversal(self):
        result = []
        if self:
            if self.Lchild:
                result.extend(self.Lchild.in_order_traversal())
                # print(result, "l")
            result.append(
                self.datum
            )  # left node --> root node --> right node recursion
            if self.Rchild:
                result.extend(self.Rchild.in_order_traversal())
                # print(result, "r")
        return result

    def deleteDeepest(self, d_node):
        q = [self]
        while q:
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.Rchild:
                if temp.Rchild is d_node:
                    temp.Rchild = None
                    return
                else:
                    q.append(temp.Rchild)
            if temp.Lchild:
                if temp.Lchild is d_node:
                    temp.Lchild = None
                    return
                else:
                    q.append(temp.Lchild)

    def deletion(self, key):
        if self is None:
            return None
        if self.Lchild is None and self.Rchild is None:
            if self.datum == key:
                return None
            else:
                return self

        key_node = None
        q = [self]
        temp = None
        while q:
            temp = q.pop(0)
            if temp.datum == key:
                key_node = temp
            if temp.Lchild:
                q.append(temp.Lchild)
            if temp.Rchild:
                q.append(temp.Rchild)
        if key_node:
            x = temp.datum
            self.deleteDeepest(temp)
            key_node.datum = x
        return self

    def search(self, value):
        if not self:
            return False
        if self.datum == value:
            return True
        found = False
        if self.Lchild:
            found = self.Lchild.search(value)
        if not found and self.Rchild:
            found = self.Rchild.search(value)

        return found

    def __str__(self):
        if (self.Lchild is None) and (self.Rchild is None):
            return f"{self.datum}"
        return f"{self.datum} (L: {self.Lchild} & R: {self.Rchild})"

    def __iter__(self):
        self._stack = []
        self._current = self
        return self

    def __next__(self):
        while self._current or self._stack:
            if self._current:
                self._stack.append(self._current)
                self._current = self._current.Lchild
            else:
                node = self._stack.pop()
                current_node = node
                self._current = node.Rchild
                # print(current_node.datum)
                return current_node

        raise StopIteration
