    #      4
    #    /   \
    #   2     7
    #  / \   /
    # 1   3 6


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

def preOrder(root):
    if root == None:
        return
    print root.info,
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    #  My problem is this BinarySearchTree class
    #  doesnt have variables that I can interact with
    #  approriately.
    #  like if self.left: do something. I only have those
    #  variables in the Node class.

    #Node is defined as
    #self.left (the left child of the node)
    #self.right (the right child of the node)
    #self.info (the value of the node)
    def insert(self,r,val):

        if r is None:
            self.r = Node('')
            self.r.info = val
        elif val < r.info:
            if r.left is None:
                r.left = Node('')
                r.left.info = val
            else:
                self.insert(r.left, val)
        else:
            if r.right is None:
                r.right = Node('')
                r.right.info = val
            else:
                self.insert(r.right, val)
        #  This return below returns the root of the tree.
        #  Every single time.
        return self.r

tree = BinarySearchTree()

# t = range(20)
sample = [4,2,3,1,7,6]

#  unsure what the r argument will be?
r = None

for i in sample:
    r = tree.insert(r,i)

preOrder(tree.r)