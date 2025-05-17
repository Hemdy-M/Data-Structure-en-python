# Data structure : tree (binary tree)
class BinaryTree:
    def __init__(self, val: int, **kwargs) -> None:
        self.val: int = val
        try:
            self.left: BinaryTree = kwargs.get("left")
        except:
            self.left: None = None
        
        try:
            self.right: BinaryTree = kwargs.get("right")
        except:
            self.right: None = None
        
        self.output: list[int] = []

    def preorderCheck(self, root) -> list[int]:
        if root == None:
            return self.output
        
        self.output.append(root.val)

        if root.left != None:
            self.preorderCheck(root.left)
        if root.right != None:
            self.preorderCheck(root.right)
        return self.output

# Left branch
inner_left: BinaryTree = BinaryTree(1, right=BinaryTree(3))

# Right branch
inner_sub_right: BinaryTree = BinaryTree(4, left=BinaryTree(6))
inner_right: BinaryTree = BinaryTree(2, left=inner_sub_right, right=BinaryTree(5))

# Define the tree's root
root: BinaryTree = BinaryTree(0, left=inner_left, right=inner_right)
print(root.preorderCheck(root))