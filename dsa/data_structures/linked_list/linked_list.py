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
            #code for an empty linked list only
            self.head = Node(value, self.head)
            if len(args) == 0:
                return
            current = self.head
            for arg in args:
                new_node= Node(arg)
                switch = True
                while current and switch:
                    if current.next == None:
                        print("inside the if statement")
                        current.next = new_node
                        current = new_node
                        switch = False
                    else:
                        current = current.next
            return
        # code for linked list with self.head
        new_node = Node(value)
        current = self.head
        # loop through the linked list until current.next == None
        while current.next != None:
            current = current.next
        current.next = new_node
        current = new_node
        #checks if there are any arguments after the value
        if len(args)== 0:
            return
        for arg in args:
            new_node = Node(arg)
            current.next = new_node
            current = new_node
        return

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
    ll.insert("1","3","2")
    print(ll)
    ll.append("")







