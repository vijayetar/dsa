from dsa.data_structures.tree.tree import Queue

class Node:
    def __init__(self,value, left_ = None, right_ = None, next_ = None):
        self.value = value
        if (isinstance(left_,Node) == False and left_ != None) or (isinstance(right_,Node) == False and right_ != None):
            raise TypeError("hey there is a problem with the value")
        self.left = left_
        self.right = right_
        self.next= next_

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,value):
        '''Takes single argument and adds argument value to the Binary Tree using breadth first traversal'''
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        bt_queue = Queue()
        def evaluate_q(root_node, new_node):
            if not root_node.left:
                root_node.left = new_node
                return
            bt_queue.enqueue(root_node.left)
            if not root_node.right:
                root_node.right = new_node
                return
            bt_queue.enqueue(root_node.right)
            root_node = bt_queue.dequeue()
            evaluate_q(root_node,new_node)
        evaluate_q(self.root, new_node)

    def breadth_first(self):
        '''Returns list with node vlaues in breadth traversal'''
        if not self.root:
            return "NULL"
        output = []
        bt_queue = Queue()
        def evaluate_q(root_node):
            output.append(root_node.value)
            if root_node.left:
                bt_queue.enqueue(root_node.left)
            if root_node.right:
                bt_queue.enqueue(root_node.right)
            if bt_queue.isEmpty():
                return
            root_node = bt_queue.dequeue()
            evaluate_q(root_node)

        evaluate_q(self.root)
        return output

    def find_max_value(self):
        '''Finds maximum value in the binary tree and returns the number'''
        if not self.root:
            raise Exception("The tree is empty")
        max = self.root.value
        def traverse(root, max):
            if not root:
                return None
            if max < root.value:
                max = root.value
            if root.left:
                max = traverse(root.left, max)
            if root.right:
                max = traverse(root.right, max)
            return max
        max = traverse(self.root, max)
        return max


    def preOrder(self):
        '''Returns list with node values in depth first traversal in the preorder method'''
        if not self.root:
            return "NULL"
        output = []
        def walk(root_node):
            output.append(root_node.value)
            if root_node.left:
                walk(root_node.left)
            if root_node.right:
                walk(root_node.right)
        walk(self.root)
        return output

    def inOrder(self):
        '''Returns list with node values in depth first traversal in the inorder method'''
        if not self.root:
            return "NULL"
        output = []
        def walk(root_node):
            if root_node.left:
                walk(root_node.left)
            output.append(root_node.value)
            if root_node.right:
                walk(root_node.right)
        walk(self.root)
        return output

    def postOrder(self):
        '''Returns list with node values in depth first traversal in the postorder method'''
        if not self.root:
            return "NULL"
        output = []
        def walk(root_node):
            if root_node.left:
                walk(root_node.left)
            if root_node.right:
                walk(root_node.right)
            output.append(root_node.value)
        walk(self.root)
        return output

    def __str__(self):
        if not self.root:
            return "NULL"
        self.final_string = ""
        def bt_output(root_node):
            self.final_string+= f"{root_node.value}--> "
            if root_node.left:
                bt_output(root_node.left)
            if root_node.right:
                bt_output(root_node.right)
            return
        bt_output(self.root)
        return f"{self.final_string}NULL"
