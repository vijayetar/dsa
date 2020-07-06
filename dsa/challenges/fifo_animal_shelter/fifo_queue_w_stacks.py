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

if __name__ == "__main__":
    my_shelter  = AnimalShelter()
    my_shelter.add_animal("dog", "fido")
    my_shelter.add_animal("cat", "feline")
    my_shelter.add_animal("otter", "sir")
    print(my_shelter)
    print(my_shelter.remove_animal("other"))
    print(my_shelter)
