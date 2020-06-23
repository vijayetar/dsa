from dsa.data_structures.tree.tree import BinaryTree2

def find_intersection(tree1, tree2):
    '''
    Function to find the intersection of the values between two binary trees and return the values as a list
    '''
    if not tree1.root and not tree2.root:
        raise ValueError ("No trees inserted")
    elif not tree1.root or not tree2.root:
        raise Exception ("One empty tree inserted, so no intersections found")
    returned_list = []
    bt1_list = tree1.postOrder()
    def walk_here(root_node):
            if root_node.value in bt1_list:
                returned_list.append(int(root_node.value))
            if root_node.left:
                walk_here(root_node.left)
            if root_node.right:
                walk_here(root_node.right)
    walk_here(tree2.root)
    return returned_list








if __name__ == "__main__":
    tree1 = BinaryTree2()
    tree2 = BinaryTree2()
    tree1.add("1")
    tree2.add("1")
    tree1.add("10")
    tree2.add("10")
    tree1.add("3")
    tree2.add("3")
    # tree1.add("7")
    print(find_intersection(tree1, tree2))
