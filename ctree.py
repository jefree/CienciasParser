class Node(object):
    
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = None
        
    def add_child(self, value):
        if not self.children:
            self.children = []

        new_node = Node(value, self)
        self.children.append(new_node)

        return new_node

    def is_leaf(self):
        return self.children == None

class Tree(object):
    
    def __init__(self, root):
        self.root = Node(root, None)

    def preorder(self, node=None, spaces=''):
        if (node == None):
            node = self.root

        print(spaces+node.value)

        if (node.children == None):
            return

        for child in node.children:
            self.preorder(child, spaces+"  ")