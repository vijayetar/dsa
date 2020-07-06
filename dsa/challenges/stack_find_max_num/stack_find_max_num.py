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








if __name__ == "__main__":
   my_numbers = Int_Stack()
   print(my_numbers.add_num(30))
   print(my_numbers.add_num(28))
   print(my_numbers.add_num(100))
   print(my_numbers.add_num(15))
   print(my_numbers.add_num(-4))
   print(my_numbers)
   print(my_numbers.find_max())
