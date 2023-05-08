class binary_tree:
    def __init__(self, key):
        self.leftchild = None
        self.rightchild = None
        self.key = key

    def add(self, value):
        if self.key is None:
            self.key = value
            return
        if self.key == value:
            return
        if value < self.key:
            if self.leftchild:
                self.leftchild.add(value)
            else:
                self.rightchild = binary_tree(value)
        else:
            if self.rightchild:
                self.rightchild.add(value)
            else:
                self.rightchild = binary_tree(value)

    def search(self, value):
        if self.key == value:
            print('The node is present')
            return
        if value < self.key:
            if self.leftchild:
                self.leftchild.search(value)
            else:
                print('The node is empty in the tree')
        else:
            if self.rightchild:
                self.rightchild.search(value)
                return True
            else:
                print('The node is empty in the tree')

    def check(self, value):
        if self.key is None:
            self.key = value

    class binary_tree:
        def __init__(self):
            self.root = None


root = binary_tree(56)
elements = {20, 56, 3, 4, 7, 10, 17, 20}
for i in elements:
    root.add(i)
root.search(56)
