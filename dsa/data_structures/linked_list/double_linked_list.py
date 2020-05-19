class LinkedList():
    def __init__ (self, head):
        self.head = head

    # def insert(self, new_value):
    #     self.head = Node(new_value, self.head)



class Node():
    def __init__ (self, value, next_=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next_

    def set_next(self, next_):
        self.next = next_

    def set_prev(self,prev):
        self.prev = prev

    def __str__(self):
        return f"{self.prev}: {self.value}: {self.next}"

    def __repr__(self):
        return f"{self.prev}: {self.value}: {self.next}"

if __name__ == "__main__":
    apples = Node("apples")
    print(apples)
    bananas = Node("bananas")
    print(bananas)
    bananas.set_next("coconut")
    # fruitbasket = LinkedList("fruitbasket")
    # print(fruitbasket.head)
    # bananas.next = apples.value
    # print(bananas)
    # apples.prev = bananas.value
    print(apples)
    print(bananas)

