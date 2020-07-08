#stacks and queues
import pysnooper

class Node:
    def __init__ (self,value, _next=None):
        self.value = value
        self.next = _next

    def __str__(self):
        return self.value

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value, *args):
        '''adds value to the top of the stack'''
        node_list = [value] + list(args)
        current = self.top
        for arg in node_list:
            current = Node(arg,current)
        self.top = current
        return

    def isEmpty(self):
        '''returns Boolean if the stack is empty'''
        if not self.top:
            return True
        return False

    def peek(self):
        '''returns the value of the top of the stack'''
        if not self.top:
            raise Exception("Empty")
        return self.top.value

    def pop(self):
        '''returns the value of the top of the stack'''
        if not self.top:
            raise Exception("Empty")
        current = self.top
        self.top = current.next
        return current.value

    def __str__(self):
        current = self.top
        str = ""
        while current:
            str += f"{{{current.value}}}-->"
            current= current.next
        return f"{str} None"


class Queue_w_stacks:
    '''create Queue class using two Stacks'''
    def __init__(self):
        self.stack2dequeue = Stack()
        self.stack2enqueue = Stack()

    def isEmpty(self):
        return self.stack2dequeue.isEmpty()

    def peek(self):
        return self.stack2dequeue.peek()

    def enqueue(self, value, *args):
        '''when we enqueue, we add to the tail, so that the tail moves to the top of the stack with every addition'''
        while not self.stack2dequeue.isEmpty():
            self.stack2enqueue.push(self.stack2dequeue.pop())
        self.stack2enqueue.push(value, *args)

    def dequeue(self):
        ''' to dequeue requires that everything is moved from stack2enqueue to stack2dequeue'''
        while not self.stack2enqueue.isEmpty():
            self.stack2dequeue.push(self.stack2enqueue.pop())
        return self.stack2dequeue.pop()

    def __str__(self):
        while not self.stack2enqueue.isEmpty():
            self.stack2dequeue.push(self.stack2enqueue.pop())
        return str(self.stack2dequeue)


class AnimalShelter(Queue_w_stacks):
    def add_animal(self, type, name):
        self.enqueue([type,name])
    def remove_animal(self, type):
        while not self.stack2enqueue.isEmpty():
            self.stack2dequeue.push(self.stack2enqueue.pop())
        while not self.stack2dequeue.isEmpty():
            arr = self.stack2dequeue.pop()
            if (type in ['cat', 'dog'] and arr[0] == type) or (type not in ['cat', 'dog'] and arr[0] not in ['cat', 'dog']):
                while not self.stack2dequeue.isEmpty():
                    self.stack2enqueue.push(self.stack2dequeue.pop())
                break
            self.stack2enqueue.push(arr)
        return arr


class Queue:
    '''standard Queue'''
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value, *args):
        '''adds value to the back of the queue'''
        if self.isEmpty():
            self.front = self.rear = Node(value)
            node_list = list(args)
        else:
            node_list = [value]+list(args)
        current = self.rear
        for arg in node_list:
            current.next = Node(arg)
            current = current.next
        self.rear = current

    def isEmpty(self):
        '''returns Boolean if the stack is empty'''
        if not self.front:
            return True
        return False

    def peek(self):
        '''returns the value of the front of the queue'''
        if not self.front:
            raise Exception("Empty Queue")
        return self.front.value

    def dequeue(self):
        '''removes the front of the queue, and returns the value'''
        if not self.front:
            raise Exception("Empty Queue")
        current = self.front
        self.front= current.next
        return current.value

    def __str__(self):
        current = self.front
        str = ""
        while current:
            str += f"{{{current.value}}}-->"
            current= current.next
        return f"{str} None"

class Int_Stack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self._max_stack = Stack()

    def add_num(self, num):
        if not isinstance(num, int):
            return "please enter num only"
        if self._max_stack.isEmpty():
            self._max_stack.push(num)
        else:
            if self._max_stack.peek()<num:
                self._max_stack.push(num)
        self.push(num)
        return

    def find_max(self):
        if self._max_stack.isEmpty():
            return "no number available in stack"
        return self._max_stack.peek()

def EMMM(arr, num):
    if not arr or not isinstance(num, int):
        return "enter correct array and num"
    def walk(arr,num,i):
        if len(arr)==1:
            return
        mod = num % len(arr)
        new = mod-1+i
        arr.remove(arr[new])
        if new >= len(arr):
            new = new-len(arr)
        walk(arr,num,new)
    walk(arr,num,0)
    return arr[0]

class TreeNode():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value} -->l{self.left} -->r{self.right}"

class BinaryTree():
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

    def find_max(self):
        if not self.root:
            return ("Empty tree")
        max = float('-inf')
        def walk(root, max):
            if not root:
                return max
            if root.value >max:
                max = root.value
            max = walk(root.left, max)
            max = walk(root.right, max)
            return max
        max = walk(self.root, max)
        return max

    def to_fizzbuzz(self):
        def fizzbuzz(value):
            if value%3 == 0 and value%5 ==0:
                return "FizzBuzz"
            elif value%3 ==0:
                return "Fizz"
            elif value%5 ==0:
                return "Buzz"
            return string(value)
        if not self.root:
            return ("Empty tree")
        def walk(root):
            if not root:
                return
            root.value=fizzbuzz(root.value)
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def add_root(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        def walk(root, value):
            if not root:
                return
            if value < root.value:
                if not root.left:
                    root.left = TreeNode(value)
                    return
                else:
                    walk(root.left, value)
            elif value >root.value:
                if not root.right:
                    root.right = TreeNode(value)
                    return
                else:
                    walk(root.right, value)
        walk(self.root, value)
        return

    def contains(self,value):
        if not self.root:
            return ("empty tree")
        def walk(root, value):
            if not root:
                return False
            if value == root.value:
                return True
            if value < root.value:
                if_contains = walk(root.left, value)
            if value > root.value:
                if_contains = walk(root.right, value)
            return if_contains
        if_contains = walk(self.root, value)
        return if_contains

    def add_value(self,value):
        if not self.root:
            return ("Empty tree")
        def walk(root):
            if not root:
                return
            root.value+= value
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return



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

def fizzbuzztree(tree):
    if not tree.root:
        return ("empty tree")
    def fizzbuzz(value):
        if value%3 == 0 and value%5 ==0:
            return "FizzBuzz"
        elif value%3 ==0:
            return "Fizz"
        elif value%5 ==0:
            return "Buzz"
        return string(value)
    def walk(root):
        if not root:
            return
        new_root_value = fizzbuzz(root.value)
        new_node = TreeNode(new_root_value)
        new_tree.add_root(new_node)
        new_node.left = walk(root.left)
        new_node.right= walk(root.right)
        return new_node
    new_tree = BinaryTree()
    new_tree.root = walk(tree.root)
    return new_tree.root

def check_files(tree1, tree2):
    if not tree1.root and not tree2.root:
        return "Empty trees"
    elif not tree1.root or not tree2.root:
        return False
    def walk(root, counter=0):
        if not root:
            return counter
        if root.value == "file":
            counter += 1
        counter = walk(root.left, counter)
        counter = walk(root.right, counter)
        return counter
    return walk(tree1.root)==walk(tree2.root)

def odd_sums(tree1):
    if not tree1.root:
        return "Empty Tree"
    def walk(root, sum = 0):
        if not root:
            return sum
        if root.value%2 !=0:
            sum += root.value
        sum = walk(root.left,sum)
        sum = walk(root.right,sum)
        return sum
    sum = walk(tree1.root)
    return sum

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         temp = arr[i]
#         position =i
#         while position>0 and arr[position-1]>temp:
#             arr[position]=arr[position-1]
#             position = position-1
#         arr[position]=temp
#     return arr

# def merge_sort(arr):
#     def merge(arr, left, right):
#         print(arr,left,right)
#         i=0
#         j=0
#         k=0
#         while i<len(left) and j<len(right):
#             if left[i]<right[i]:
#                 arr[k]=left[i]
#                 i+=1
#             else:
#                 arr[k]=right[j]
#                 j+=1
#             k+=1
#         if i<=len(left)-1:
#             for i in range(i, len(left)):
#                 arr[k]=left[i]
#                 k+=1
#         if j<=len(right)-1:
#             for j in range(j, len(right)):
#                 arr[k]=right[j]
#                 k+=1
#         return arr
#     if len(arr)>1:
#         mid = len(arr)//2
#         print(mid)
#         #sort the left
#         left = arr[0:mid]
#         left = merge_sort(left)
#         #sort the right
#         right = arr[mid:len(arr)]
#         right = merge_sort(right)
#         merge(arr, left, right)
#     return arr

def insertion_sort(arr):
    for i in range (1, len(arr)):
        position = i
        while arr[position]<arr[position-1] and position>0:
            arr[position],arr[position-1]=arr[position-1],arr[position]
            position-=1
    return arr

def merge_sort2(arr):
    def merge(arr,left,right):
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            elif right[j]<left[i]:
                arr[k]=right[j]
                j+=1
            k+=1
        if i<len(left):
            for i in range(i,len(left)):
                arr[k]=left[i]
                k+=1
        if j<len(right):
            for j in range(j, len(right)):
                arr[k]=right[j]
                k+=1
        return arr
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort2(left)
        right = merge_sort2(right)
        arr = merge(arr,left,right)
    return arr

def quick_sort(arr, left=0, right=None):
    def swap(arr, i, low):
        arr[i], arr[low] = arr[low], arr[i]
        return
    def partition(arr, left, right):
        pivot = arr[right]
        low = left-1
        for i in range(left,right):
            if arr[i]<=pivot:
                low=low+1
                swap(arr,i,low)
        swap(arr,right,low+1)
        return low+1

    if right==None:
        right = len(arr)-1
    if left<right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position-1)
        quick_sort(arr, position+1, right)
    return arr

def insertion_sort2(arr):
    for i in range(1,len(arr)):
        position = i
        while arr[position-1]>arr[position] and position>0:
            arr[position],arr[position-1]=arr[position-1],arr[position]
            position-=1
    return arr

def merge_sort3(arr):
    def merge(arr,left,right):
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            elif right[j]<left[i]:
                arr[k]=right[j]
                j+=1
            k+=1
        if i<len(left):
            for i in range(i,len(left)):
                arr[k]=left[i]
                k+=1
        if j<len(right):
            for j in range(j,len(right)):
                arr[k]=right[j]
                k+=1
        return arr
    if len(arr)>1:
        mid=len(arr)//2
        left = merge_sort3(arr[:mid])
        right = merge_sort3(arr[mid:])
        merge(arr,left,right)
    return arr

def quick_sort2(arr, left=0, right=None):
    def partition(arr,left,right):
        pivot = arr[right]
        low = left-1
        for i in range(right):
            if arr[i]<pivot:
                low+=1
                arr[low],arr[i]=arr[i],arr[low]
        arr[low+1],arr[right]=arr[right],arr[low+1]
        return low+1


    if right==None:
        right = len(arr)-1
    if left<right:
        pos = partition(arr,left,right)
        quick_sort2(arr,left,pos-1)
        quick_sort2(arr,pos+1,right)
    return arr


def hash(string):
    hashed_key = (sum(map(lambda x: ord(x), string))*19) %100
    print(hashed_key)

def graph_list_to_matrix():
    adj= {"a":[1], "b":[2], "c":[3]}
    print(len(adj))
    print([[None]*len(adj)]*len(adj))

# @pysnooper.snoop()

def find_leaf_weight(tree, int):
    if not tree.root:
        return "No Tree provided"
    result = 0
    def walk(root, sum=0, switch=False):
        if not root:
            return sum, switch
        sum += root.value
        if not root.left and not root.right and int == sum:
            switch = True
            return sum, switch
        if not switch:
            sum, switch = walk(root.left, sum, switch)
        if not switch:
            sum, switch = walk(root.right, sum, switch)
        if not switch:
            sum = sum - root.value
        return sum, switch

    result, switch = walk(tree.root)
    return result, switch




# def find_leaf_weight2(tree, int):
# 	if not tree.root:
# 		return "NO tree"
# 	result=0
# 	def walk(root, sum=0, switch=False):
# 		if not root:
# 			return sum, switch
# 		sum += root.value
#         if not root.left and not root.right:
#             if int==sum:
# 			    switch = True
# 			    return sum, switch
#         elif not switch:
# 			sum, switch = walk(root.left, sum, switch)

#         if not switch:
# 			sum, switch = walk(root.right, sum, switch)

#         if not switch:
# 		    sum = sum - root.value
# 		return sum, switch

# 	result, switch = walk(tree.root)
# 	return result, switch





if __name__ == "__main__":
    # graph_list_to_matrix()
    # arr = [100, 20, 50, 30, 40, 10]
    # print(insertion_sort2(arr))
    # print(merge_sort3(arr))
    # print(quick_sort2(arr))
    numbers1 = BinaryTree()
    numbers1.add_root(1)
    numbers1.add_root(10)
    numbers1.add_root(10)
    numbers1.add_root(100)
    numbers1.add_root(100)
    numbers1.add_root(100)
    numbers1.add_root(100)
    numbers1.add_root(1000)
    numbers1.add_root(1000)
    print(find_leaf_weight(numbers1,1111))
    # print(odd_sums(numbers1))
    # numbers2 = BinaryTree()
    # numbers2.add_root('folder')
    # numbers2.add_root('folder')
    # numbers2.add_root('file')
    # # numbers2.add_root('file')
    # # numbers2.add_root('file')
    # print(check_files(numbers1, numbers2))




