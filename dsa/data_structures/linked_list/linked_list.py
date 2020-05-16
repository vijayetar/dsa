class LinkedList:
    linked_list= []

# create Node class and instantiate it with value and pointer
class Node:
    def __init__ (self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"This is {self.value} instantiated in Node class"

    def __repr__(self):
        return self.value


if __name__ == "__main__":
    apples = Node("apples")
    print(apples)
    print(apples.next)
