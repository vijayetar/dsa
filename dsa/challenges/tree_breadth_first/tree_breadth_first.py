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
    bt.add("44")
    bt.add("apples")
    bt.add(100)
    bt.add("bananas")
    bt.add(120)
    bt.add("kiwi")
    bt.add("lastOne")
    bt.add("testlastOne")
    print("**********"*5)
    print(bt.breadth_first())
