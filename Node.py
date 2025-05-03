class RedBlackNode:
    def __init__(self, value,color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    #get the grandparent
    def grandparent(self):
        if self.parent is None:
            return None
        else:
            return self.parent.parent

    #get the brother will help to get the uncle
    def sibling(self):
        if self.parent is None:
            return None
        if self.parent.left == self:
            return self.parent.right
        else:
            return self.parent.left

    #get the uncle of the node(sibling of the parent)
    def uncle(self):
        if self.parent is None:
            return None
        else:
            return self.parent.sibling()