from Lab3.Node import RedBlackNode


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def search(self,value):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.value == value:
                return curr_node
            elif curr_node.value > value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None

    #small value go left , big value go right
    def insert(self,value):
        new_node = RedBlackNode(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while True:
                if value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.right
        self.size += 1
        self.insert_fix(new_node)



    def insert_fix(self,new_node):
            while new_node.parent and new_node.parent.color=='red':
                # check if we're dealing with the left subtree so we will need to rotate right the grandparent
                if new_node.parent == new_node.grandparent().left:
                    uncle = new_node.uncle()
                    #case uncle is red
                    if uncle and uncle.color=='red':
                        new_node.parent.color = 'black'
                        uncle.color = 'black'
                        new_node.grandparent().color = 'red'
                        new_node = new_node.grandparent() # Move up to fix violation maybe happen
                    else:
                        # case uncle is black
                        if new_node == new_node.parent.right:
                            new_node = new_node.parent
                            self.rotate_left(new_node)# fix the triangle shape to line on the left
                        new_node.parent.color = 'black'
                        new_node.grandparent().color = 'red'
                        self.rotate_right(new_node.grandparent())
                else:
                    #dealing with the Right subtree so we will need to rotate Left the grandparent
                    uncle = new_node.uncle()
                    if uncle and uncle.color == 'red':
                        new_node.parent.color = 'black'
                        uncle.color = 'black'
                        new_node.grandparent().color = 'red'
                        new_node = new_node.grandparent()# Move up to fix violation maybe happen
                    else:
                        if new_node == new_node.parent.left:
                            new_node = new_node.parent
                            self.rotate_right(new_node)# fix the triangle shape to line on the right
                        new_node.parent.color = 'black'
                        new_node.grandparent().color = 'red'
                        self.rotate_left(new_node.grandparent())
            self.root.color = 'black'

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def get_tree_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_tree_height(node.left), self.get_tree_height(node.right))

    def get_black_height(self, node):
        if node is None:
            return 0
        left_black_height = self.get_black_height(node.left)# right or left no difference RBT rules
        if node.color == 'black':
            return 1 + left_black_height
        else:
            return left_black_height

    def get_tree_size(self):
        return self.size

    def print_tree_height(self):
        print("Tree Height:", self.get_tree_height(self.root))

    def print_black_height(self):
        print("Black Height:", self.get_black_height(self.root))

    def print_tree_size(self):
        print("Tree Size:", self.get_tree_size())