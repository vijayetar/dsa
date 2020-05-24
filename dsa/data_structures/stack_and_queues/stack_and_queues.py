from collections import deque

class Node:
    def __init__ (self, value, next_ = None):
        self.value = value
        if not isinstance(next_,Node) and next_ != None:
            raise TypeError("hey there is a problem with the value")
        self.next = next_

    def __str__(self):
        return f"{self.value} : {self.next}"

    def __repr__(self):
        return f"{self.value} : {self.next}"

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
            next_value, current.next = current.next, None
            self.top = next_value
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

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_value):
        '''Takes any value as an argument and adds a new node with that value to the back of the queue '''
        if self.isEmpty():
            self.rear = Node(new_value)
            self.front = self.rear
            return
        current = self.rear
        current.next = Node(new_value)
        self.rear = current.next
        return

    def dequeue(self):
        '''Removes the node from the front of the queue, and returns the node’s value.'''
        if not self.front:
            raise Exception("this is an empty Queue")
        current = self.front
        if current.next:
            self.front = current.next
            current.next = None
        else:
            self.front = None
            self.rear = None
        return current.value

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

class QueueDeque():
    def __init__(self):
        self.storage = deque()
    def enqueue(self,new_value):
        if len(self.storage):
            new_node = Node(new_value, self.storage[0])
            print("this is in self.storage", self.storage)
            self.storage.appendleft(new_node)
        else:
            self.storage.appendleft(Node(new_value))
        return
    def dequeue(self):
        return self.storage.pop()
    def peek(self):
        return self.storage[-1]
    def is_empty(self):
        return len(self.storage)==0
    def __str__(self):
        '''String representation of QueueDeque '''
        final_string = ""
        for item in self.storage:
            final_string += f"<- {{{str(item.value)}}}"
        return f"NULL{final_string}"


if __name__ == "__main__":
    my_queue = QueueDeque()
    print(str(my_queue))
    my_queue.enqueue("task1")
    my_queue.enqueue("task2")
    my_queue.enqueue("task3")
    my_queue.enqueue("task4")
    print(str(my_queue))




