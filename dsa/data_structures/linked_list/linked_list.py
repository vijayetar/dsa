from abc import ABC, abstractmethod

# makes the head of a LinkedList by connecting it to the name of the LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, *args):
        self.head = Node(value, self.head)
        for arg in args:
            self.head = Node(arg, self.head)
        return self

    def append(self,value, *args):
        # checks if the self.head has a value
        if not self.head:
            self.head = Node(value, self.head)
            print('this is self.head',self.head)
            if len(args) == 0:
                return
            current = self.head
            print("this is length of args", len(args))
            for arg in args:
                print('this is the arg', arg)
                new_node= Node(arg)
                print('this is the new_node', new_node)
                switch = True
                while current and switch:
                    print("this is current",current, switch)
                    print("this is current.next",current.next)
                    if current.next == None:
                        print("inside the if statement")
                        current.next = new_node
                        current = new_node
                        switch = False
                    else:
                        current = current.next
                    print("this is the new current",current)
        # new_node = Node(value)
        # current = self.head
        # # checks if the next value is None or Falsy
        # if not current.next:
        #     new_node.next, current.next = current.next, new_node
        #     return
        # while current.next:
        #     current = current.next
        #     if not current.next:
        #         new_node.next, current.next = current.next, new_node
        #         return

    def __str__(self):
        """ { a } -> { b } -> { c } -> NULL """

        final_string = ""

        current = self.head

        while current:
            final_string += f"{{{current.value}}} -> "
            current = current.next

        return f"{final_string} NULL"

    def includes(self,value):
        """ check if value entered is present in the linked list """
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False


# create Node class and instantiate it with value and pointer
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


if __name__ == "__main__":

    ll = LinkedList()
    print(ll)
    ll.append("Kite", "Lucky", "Lucy")
    print(ll)
    # ll.append("L","1","2","3")
    # print(ll)
    # ll.append("L","u","c","k","y")
    # print(ll)
    # ll.append("Merv")
    # print(ll)
    # ll.append("Naomi")
    # print(ll)





