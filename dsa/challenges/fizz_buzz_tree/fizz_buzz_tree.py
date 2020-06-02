from dsa.data_structures.tree.tree import Node, Queue

def fizz_buzz_tree(bt):
    if not isinstance(bt, BinaryTree):
        raise ValueError ("this is not a Tree")
    elif not bt.root:
        raise Exception ("the argument has no root")

    fb_bt = BinaryTree()

    def fizz_buzz(num):
        if not num%5 and not num%3:
            return 'FizzBuzz'
        elif not num%5:
            return 'Buzz'
        elif not num%3:
            return 'Fizz'
        else:
            return str(num)

    def walk(root_node):
        if not root_node.value:
            return
        output = fizz_buzz(root_node.value)
        fb_bt.add(output)
        print("this is the tree", fb_bt)
        if root_node.left:
            walk(root_node.left)
        if root_node.right:
            walk(root_node.right)
    walk(bt.root)
    return fb_bt


class BinaryTree:
    def __init__(self):
        self.root = None

    # def add(self,value):
    #     '''Takes single argument and adds argument value to the Binary Tree'''
    #     new_node = Node(value)
    #     if not self.root:
    #         self.root = new_node
    #         return
    #     def walk(root_node, new_node):
    #         if not root_node:
    #             return
    #         if root_node.left == None:
    #             root_node.left = new_node
    #             return
    #         elif root_node.right == None:
    #             root_node.right = new_node
    #             return
    #         else:
    #             walk(root_node.left, new_node)
    #             walk(root_node.right, new_node)
    #     walk(self.root,new_node)
    #     return

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

if __name__ == "__main__":
    bt_full = BinaryTree()
    bt_full.add(15)
    bt_full.add(45)
    bt_full.add(27)
    bt_full.add(22)
    bt_full.add(60)
    bt_full.add(33)
    print(bt_full.preOrder())
    tree = fizz_buzz_tree(bt_full)
    print(tree)

