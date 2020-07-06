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
        '''
        prints out the tree in depth first manner
        '''
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

class BinaryTree2:
    def __init__(self):
        self.root = None

    def add(self,value):
        '''Takes single argument and adds argument value to the Binary Tree using breadth first traversal'''
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        q = []
        q.append(self.root)
        while len(q):
            root_node = q[0]
            q.pop(0)
            if not root_node.left:
                root_node.left = Node(value)
                return
            q.append(root_node.left)
            if not root_node.right:
                root_node.right = Node(value)
                return
            q.append(root_node.right)
        traverse(self.root)

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

class BinaryTree3():
    def __init__(self):
        self.root = None
    def add_root_w_args(self, value, *args):
        if not self.root:
            self.root = TreeNode(value)
            node_list = list(args)
        else:
            node_list = [value]+list(args)
        bt_queue = Queue()
        bt_queue.enqueue(self.root)
        for arg in node_list:
            switch = True
            while switch:
                current = bt_queue.dequeue()
                if not current.left and switch == True:
                    current.left = TreeNode(arg)
                    switch = False
                bt_queue.enqueue(current.left)
                print("this is bt_queue", bt_queue)
                if not current.right and switch == True:
                    current.right = TreeNode(arg)
                    switch = False
                bt_queue.enqueue(current.right)

    def add_root(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        bt_list = [self.root]
        while bt_list:
            current = bt_list.pop(0)
            if not current.left:
                current.left = TreeNode(value)
                return
            bt_list.append(current.left)
            if not current.right:
                current.right = TreeNode(value)
                return
            bt_list.append(current.right)

    def preOrder(self):
        if not self.root:
            return ("Emtpy Tree")
        output = []
        def walk(root_node):
            if not root_node:
                return
            output.append(root_node.value)
            walk(root_node.left)
            walk(root_node.right)
        walk(self.root)
        return output

    def inOrder(self):
        if not self.root:
            return ("empty tree")
        output = []
        def walk(root_node):
            if not root_node:
                return
            walk(root_node.left)
            output.append(root_node.value)
            walk(root_node.right)
        walk(self.root)
        return output

    def postOrder(self):
        if not self.root:
            return ("empty tree")
        output = []
        def walk(root_node):
            if not root_node:
                return
            walk(root_node.left)
            walk(root_node.right)
            output.append(root_node.value)
        walk(self.root)
        return output

    def breadth_first(self):
        if not self.root:
            return ("empty tree")
        output = [self.root]
        counter = 0
        length = len(output)
        while counter < len(output):
            current = output[counter]
            if current.left:
                output.append(current.left)
            if current.right:
                output.append(current.right)
            counter +=1
        output = [i.value for i in output]
        return output


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def add(self, value):
        '''Takes argument an integer and adds to the Binary Search tree so that if it is less than the root, it is placed left, and if it is more than the root, then it is placed rightof the root'''
        try:
            value = int(value)
            new_node = Node(value)
            if not self.root:
                self.root = new_node
                return
            def evaluate_value(root_node, new_node):
                if root_node.value > new_node.value:
                    if not root_node.left:
                        root_node.left = new_node
                        return
                    evaluate_value(root_node.left, new_node)
                    return
                elif root_node.value< new_node.value:
                    if not root_node.right:
                        root_node.right = new_node
                        return
                    evaluate_value(root_node.right, new_node)
                    return
            evaluate_value(self.root, new_node)
            return
        except ValueError:
            return "Binary Search Tree can only take integers"

    def contains(self, value):
        '''Takes a single argument an integer value and returns Boolean if the Binary Search Tree contains the value'''
        try:
            value = int(value)
            if not self.root:
                return "Binary Search Tree is empty"
            present = False
            def check_value(root_node, value):
                if root_node.value == value:
                    return True
                if root_node.left:
                    present = check_value(root_node.left, value)
                    if present:
                        return present
                if root_node.right:
                    present = check_value(root_node.right, value)
                    if present:
                        return present
                return False
            present = check_value(self.root, value)
            return present
        except ValueError:
            return "Binary Search Tree contains only take integers"

    def __str__(self):
        if not self.root:
            return "NULL"
        self.final_string = ""
        def bst_output(root_node):
            self.final_string+= f"{root_node.value}--> "
            if root_node.left:
                bst_output(root_node.left)
            if root_node.right:
                bst_output(root_node.right)
            return
        bst_output(self.root)
        return f"{self.final_string}NULL"

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        '''Takes any node as an argument and adds it to the back of the queue '''
        if self.isEmpty():
            self.rear = new_node
            self.front = self.rear
            return
        current = self.rear
        current.next = new_node
        self.rear = current.next
        return

    def dequeue(self):
        '''Removes the node from the front of the queue, and returns the node'''
        if not self.front:
            raise Exception("this is an empty Queue")
        current = self.front
        print("this is the current in the dequeue method", current.value)
        # if current.value == "testlastOne":
            # breakpoint()
        if current.next:
            self.front = current.next
            current.next = None
        else:
            self.front = None
            self.rear = None
        return current

    def peek(self):
        '''Returns the value of the node located in the front of the queue'''
        if self.isEmpty():
            raise Exception("sorry, the Queue is empty")
        return self.front.value

    def isEmpty(self):
        '''returns True if the Queue is empty '''
        if not self.front:
            return True
        return False

    def __str__(self):
        """ { a } -> { b } -> { c } -> NULL """

        final_string = ""

        current = self.front

        while current:
            final_string += f"{{{current.value}}} -> "
            current = current.next

        return f"{final_string}NULL"

if __name__ == "__main__":
    bt = BinaryTree()
    bt.add("root")
    bt.add("V1")
    bt.add("V2")
    bt.add("V3")
    bt.add("V4")
    bt.add("V5")
    print("**********"*5)
    print(bt.inOrder())
