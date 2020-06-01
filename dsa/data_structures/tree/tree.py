class Node:
    def __init__(self,value, left_ = None, right_ = None):
        self.value = value
        if (isinstance(left_,Node) == False and left_ != None) or (isinstance(right_,Node) == False and right_ != None):
            raise TypeError("hey there is a problem with the value")
        self.left = left_
        self.right = right_

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,value):
        #using  breadth first traversal
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        bt_queue = Queue()
        def evaluate_q(root_node, new_node):
            if root_node.left == None:
                root_node.left = new_node
                return
            bt_queue.enqueue(root_node.left)
            if root_node.right ==  None:
                root_node.right = new_node
                return
            bt_queue.enqueue(root_node.right)
            root_node = bt_queue.dequeue()
            evaluate_q(root_node,new_node)
        evaluate_q(self.root, new_node)

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


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def add(self, value):
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

    def enqueue(self, new_value):
        '''Takes any value as an argument and adds a new node with that value to the back of the queue '''
        if self.isEmpty():
            self.rear = new_value
            self.front = self.rear
            return
        current = self.rear
        current.next = new_value
        self.rear = current.next
        return

    def dequeue(self):
        '''Removes the node from the front of the queue, and returns the node’s value'''
        if not self.front:
            raise Exception("this is an empty Queue")
        current = self.front
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
    # bt = BinaryTree()
    # print("empty", bt)
    # bt.add("A")
    # print(bt)
    # bt.add("B")
    # print(bt)
    # bt.add("C")
    # print(bt)
    # bt.add("D")
    # print(bt)
    # # print("this is root",bt.root.value)
    # # my_list = bt.add("74")
    # # print(my_list)


