from dsa.data_structures.tree.tree import BinaryTree2
from dsa.challenges.hashtable.linked_list_hashtable import LinkedList

class Hashtable():
    '''
    This class is to implement the hashmap in python
    '''
    def __init__(self, size):
        self.size = size
        #this is creating a list of buckets to put the hashtable
        self.indices = [None]*self.size

    def hash(self, string):
        if not isinstance(string,str):
            string = str(string)
        hashed_key = (sum(list(map(lambda x: ord(x), string)))*19)%self.size
        return hashed_key

    def add(self, key, value):
        '''
        adding a key and value to a node of a linked list where the pair is added as an array
        '''
        hashed_key = self.hash(key)
        if not self.indices[hashed_key]:
            self.indices[hashed_key]=LinkedList()
        self.indices[hashed_key].append([key, value])

    def get(self, key):
        '''
        takes in the key and returns the value from the hashtable
        '''
        if self.contains(key):
            hashed_key= self.hash(key)
        my_list = self.indices[hashed_key].display()
        for pair in my_list:
            if pair[0]==key:
                return pair[1]

    def contains(self,key):
        '''
         takes in the key and returns a boolean, indicating if the key exists in the table already.
        '''
        hashed_key= self.hash(key)
        if not self.indices[hashed_key]:
            return False
        my_list = self.indices[hashed_key].display()
        for pair in my_list:
            if pair[0]==key:
                return True
        return False

    def __str__(self):
        switch = False
        string = ""
        for item in self.indices:
            if item:
                switch = True
                string += ("").join(str(e) for e in item.display())
        if not switch:
            return "None"
        return string
        # return self.indices


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

def find_intersection2(tree1, tree2):
    '''
    Function using hashtables to find the intersection of the values between two binary trees and return the values as a list
    '''
    if not tree1.root and not tree2.root:
        raise ValueError ("No trees inserted")
    elif not tree1.root or not tree2.root:
        raise Exception ("One empty tree inserted, so no intersections found")
    #create instance of HashTable
    bt_hashed = Hashtable(20)
    returned_list = []

    def walk_here(root_node):
            if bt_hashed.contains(root_node.value):
                returned_list.append(int(root_node.value))
            else:
                bt_hashed.add(root_node.value, value=0)
            if root_node.left:
                walk_here(root_node.left)
            if root_node.right:
                walk_here(root_node.right)
    #add each node value to the hash table
    walk_here(tree1.root)
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
    tree1.add("7")
    print(find_intersection2(tree1, tree2))
