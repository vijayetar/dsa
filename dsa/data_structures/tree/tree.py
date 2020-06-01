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

    # def add(self, value):
    #     if not self.root:
    #         self.root = Node(value)
    #         return
    #     #check left and insert there and return
    #     # or else check right and insert there and return
    #     # or reassign the root and start again
    #     new_node = Node(value)
    #     print("this is the new_node", new_node.value)

    #     # find the height of the tree on the left vs the right and then figure out where to add the new node
    #     def get_height(root):
    #         if root is None:
    #             return 0
    #         return 1 + max(get_height(root.left),get_height(root.right))

    #     def is_balanced(root):
    #         if root is None:
    #             return True
    #         return is_balanced(root.right) and is_balanced(root.left) and abs(get_height(root.left)-get_height(root.right)) <= 1

    #     def walk(root_node, new_node):
    #         if root_node.left == None:
    #             root_node.left = new_node
    #             return
    #         elif root_node.right == None:
    #             root_node.right = new_node
    #             return
    #         else:
    #             # walk(root_node.left, new_node)

    #     walk(self.root,new_node)
    #     return
    def __str__(self):
        if not self.root:
            return "NULL"
        final_string = ""
        root_node = self.root
        final_string+= f"{root_node.value}"
        def bt_output(root_node, final_string):
            final_string+= f"-->{root_node.value}"
            if root_node.left:
                bt_output(root_node.left)
            if root_node.right:
                bt_output(root_node.right)
            return final_string
        if root_node.left:
            final_string = bt_output(root_node.left, final_string)
        if root_node.right:
            final_string = bt_output(root_node.right,final_string)
        return final_string


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


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_value, *args):
        '''adds new value to the top of the stack'''
        if self.isEmpty():
            self.top = Node(new_value)
        else:
            self.top = Node(new_value, self.top)
        if len(args):
            current = self.top
            for arg in args:
                new_node = Node(arg, current)
                current = new_node
            self.top = current
        return

    def pop(self):
        '''removes the node from the top of the stack and returns the node's value'''
        if self.isEmpty():
            raise Exception("this is an empty stack")
        current = self.top
        if current.next:
            next_value = current.next
            current.next = None
            self.top = next_value
        else:
            self.top = None
        return current.value

    def isEmpty(self):
        '''returns True if the stack is empty '''
        if not self.top:
            return True
        return False

    def peek(self):
        '''returns the top value or raises exception if the stack is empty'''
        if self.isEmpty():
            raise Exception("sorry the stack is empty")
        return self.top.value

    def __str__(self):
        """ { a } -> { b } -> { c } -> NULL """

        final_string = ""

        current = self.top

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
    bst = BinarySearchTree()
    print(bst)
    bst.add("apple")
    bst.add(15)
    print(bst)
    bst.add(8)
    print(bst)
    bst.add(18)
    print(bst)
    bst.add(4)
    print(bst)
    bst.add(2)
    print(bst)
    bst.add(3)
    print(bst)
    bst.add(10)
    print(bst)
    print(bst.contains(12))

