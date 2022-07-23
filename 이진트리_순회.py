class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def pre_order(self):
        print(self.value, end=' ')
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.value, end=' ')
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.value, end=' ')


if __name__ == '__main__':
    tr4 = Tree(4, None, None)
    tr5 = Tree(5, None, None)
    tr6 = Tree(6, None, None)
    tr7 = Tree(7, None, None)
    tr2 = Tree(2, tr4, tr5)
    tr3 = Tree(3, tr6, tr7)
    tr1 = Tree(1, tr2, tr3)

    tr1.pre_order()
    print()
    tr1.in_order()
    print()
    tr1.post_order()
