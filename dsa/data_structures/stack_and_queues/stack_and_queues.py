
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

    def peek(self):
        '''returns the top value or raises exception if the stack is empty'''
        if self.isEmpty():
            raise Exception("sorry the stack is empty")
        else:
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
    my_stack = Stack()
    my_stack.push("apples")
    print(my_stack)
    my_stack.push("bananas","3","4")
    print(my_stack)
    print(my_stack.peek())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)


