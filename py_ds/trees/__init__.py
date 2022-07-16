class TreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, data):
        node = TreeNode(data)
        node.parent = self
        
        self.children.append(node)
        return node

class Tree():
    def __init__(self) -> None:
        self.root = TreeNode("root")
        self.root.children = []


    
        
    def print_tree(self, node: TreeNode) -> None:
        print(node.data)
        for child in node.children:
            self.print_tree(child)

if __name__ == "__main__":
    tree = Tree()
    n1 = tree.root.add_child("node1")
    n2 = tree.root.add_child("node2")
    n3 = tree.root.add_child("node3")
    n21 = n2.add_child("node21")
    n22 = n2.add_child("node22")
    tree.print_tree(tree.root)
