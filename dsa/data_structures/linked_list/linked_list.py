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
                        current.next = new_node
                        current = new_node
                        switch = False
                    else:
                        current = current.next
            return
        # code for linked list with self.head
        new_node = Node(value)
        current = self.head
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

    def find_k_node_value(self,k=0):
        '''Find the kth node value in the linked list from the end'''
        # check if there is a value after head
        if k < 0:
            return "Exception"
        if not self.head:
            return "Exception"
        current = self.head
        length = 1
        # find length of the linked list
        while current.next != None:
            length +=1
            current = current.next
        if k>length:
            return "Exception"
        n = length - k
        # find the value at position n
        counter = 1
        current = self.head
        while current != None:
            if n == counter:
                return current.value
            current = current.next
            counter += 1
        return "Exception"

    def find_k_node_value2(self,k=0):
        '''JB approach to finding the kth node value in the linked list from the end'''
        # check if there is a value after head
        if k < 0:
            return "Exception"
        if not self.head:
            return "Exception"
        current = self.head
        counter = 0
        while current != None:
            if counter == k:
                value_desired = self.head
            elif counter >k:
                value_desired = value_desired.next
            current = current.next
            counter+=1
        if counter > k:
            return value_desired.value
        return "Exception"

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

    # ll = LinkedList()
    # print(ll)
    # ll.append("1","3","8","2")
    # print(ll)
    # ll.append("l","i","k","e")
    # print(ll)
    # print(ll.find_k_node_value(4))
    ll= LinkedList()
    ll.insert("1","2","3")
    print(ll.find_k_node_value2(0))








