class Tree():
    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right

    def height(self, node=True):
        if node is True: node = self
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def tree_size(self, node=True):
        if node is True: node = self
        if node is None:
            return 0
        return 1 + self.tree_size(node.left) + self.tree_size(node.right)

    def add_item(self, item):
        if self.left is None:
            self.left = Tree(item)
        elif self.right is None:
            self.right = Tree(item)
        else:
            if self.tree_size(self.right) < self.tree_size(self.left):
                self.right.add_item(item)
            else:
                self.left.add_item(item)

    def scan_in_order(self, node=True):
        if node is True: node = self
        if node is None:
            return []
        return(self.scan_in_order(node.left) + [node] + self.scan_in_order(node.right))

    def scan_pre_order(self, node=True):
        if node is True: node = self
        if node is None:
            return []
        return([node] + self.scan_pre_order(node.left) + self.scan_pre_order(node.right))

    def scan_post_order(self, node=True):
        if node is True: node = self
        if node is None:
            return []
        return(self.scan_post_order(node.left) + self.scan_post_order(node.right) + [node])

    def traverse_in_order(self):
        return list(map(lambda k: k.datum, self.scan_in_order()))

    def traverse_pre_order(self):
        return list(map(lambda k: k.datum, self.scan_pre_order()))

    def traverse_post_order(self):
        return list(map(lambda k: k.datum, self.scan_post_order()))

    def __iter__(self):
        self.bucket = self.scan_in_order()
        self.curr = 0
        self.nmax = len(self.bucket)
        return self

    def __next__(self):
        if self.curr < self.nmax:
            self.curr += 1
            return self.bucket[self.curr - 1]
        raise StopIteration

    def search(self, value):
        for n in self:
            if n.datum == value:
                return True
        return False

    def __str__(self):
        if (self.left is None) and (self.right is None):
            return f"{self.datum}"
        return f"{self.datum} (L: {self.left} & R: {self.right})"

