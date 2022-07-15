class TreeNode():
    def __init__(self, data) -> None:
        self.data = None
        self.parent = None
        self.children = None



class Tree():
    def __init__(self) -> None:
        self.root = TreeNode("root")
        self.root.children = []


    def add_child(self, parent, data):
        node = TreeNode(data)
        node.children = []
        node.parent = parent
        
        parent.children.append(self)
        
        

if __name__ == "__main__":
    tree = Tree()
    tree.add_child(tree.root, "node1")
