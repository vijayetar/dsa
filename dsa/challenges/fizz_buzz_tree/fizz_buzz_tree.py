from dsa.data_structures.tree.tree import Node, Queue, BinaryTree

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

def fizz_buzz_tree2(bt):
    if not isinstance(bt, BinaryTree):
        raise ValueError ("this is not a Tree")
    elif not bt.root:
        raise Exception ("the argument has no root")

    def check_fizz_buzz(num):
        if not num%5 and not num%3:
            return 'FizzBuzz'
        elif not num%5:
            return 'Buzz'
        elif not num%3:
            return 'Fizz'
        else:
            return str(num)

    def add_fizz_buzz(value, new_bt, bt_queue):
        new_value = check_fizz_buzz(value)
        new_bt.add(new_value)
        return

    def breadth_walk(bt, new_bt):
        '''Returns list with node vlaues in breadth traversal'''
        bt_queue = Queue()
        def evaluate_q(root_node):
            add_fizz_buzz(root_node.value, new_bt, bt_queue)
            if root_node.left:
                bt_queue.enqueue(root_node.left)
            if root_node.right:
                bt_queue.enqueue(root_node.right)
            if bt_queue.isEmpty():
                return
            root_node = bt_queue.dequeue()
            evaluate_q(root_node)
        evaluate_q(bt.root)

    new_bt = BinaryTree()
    bt_queue = Queue()
    breadth_walk(bt,new_bt)
    return new_bt.breadth_first()

def fizz_buzz_tree3(bt):
    if not isinstance(bt, BinaryTree):
        raise ValueError ("this is not a Tree")
    elif not bt.root:
        raise Exception ("the argument has no root")

    def check_fizz_buzz(num):
        if not num%5 and not num%3:
            return 'FizzBuzz'
        elif not num%5:
            return 'Buzz'
        elif not num%3:
            return 'Fizz'
        else:
            return str(num)

    def traverse(root):
        '''Returns list with node vlaues in breadth traversal'''
        if not root:
            return None
        fizzy_value = check_fizz_buzz(root.value)
        new_node = Node(fizzy_value)
        new_node.left = traverse(root.left)
        new_node.right = traverse(root.right)
        return new_node

    new_bt = BinaryTree()
    new_bt.root = traverse(bt.root)
    return new_bt.breadth_first()

if __name__ == "__main__":
    bt_full = BinaryTree()
    bt_full.add(15)
    bt_full.add(45)
    bt_full.add(2)
    bt_full.add(22)
    bt_full.add(60)
    bt_full.add(33)
    bt_full.add(25)
    tree = fizz_buzz_tree2(bt_full)
    print(tree)
    tree = fizz_buzz_tree3(bt_full)
    print(tree)

