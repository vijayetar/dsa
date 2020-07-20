#stacks and queues from practice attempt in July 2020

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
            raise Exception("Empty Stack")
        return self.top.value

    def pop(self):
        '''returns the value of the top of the stack'''
        if not self.top:
            raise Exception("Empty Stack")
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

class Queue:
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


if __name__ == "__main__":
    dishes = Queue()
    print(dishes.isEmpty())
    dishes.enqueue("veges", "grapes", "bananas")
    dishes.enqueue("sweets", "icecream")
    print(dishes)
    print("this is peeking", dishes.peek())
    print("this is rear", dishes.rear)
    print("pop", dishes.dequeue())
    print("pop", dishes.dequeue())
    print("pop", dishes.dequeue())
    print("pop", dishes.dequeue())
    print(dishes)



