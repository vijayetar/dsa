
#doubly linked list

class Node:
    def __init__ (self,value, _next=None, _back=None):
        self.value = value
        self.next = _next
        self.back = _back

    def __str__(self):
        return self.value

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self,value, *args):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value,self.head)
            self.head.back = new_node
            self.head = new_node
        for arg in args:
            new_node = Node(arg,self.head)
            self.head.back = new_node
            self.head = new_node
        return self.head

    def includes(self,value):
        current = self.head
        while current.next:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value, *args):
        new_node = Node(value, None, self.tail)
        self.tail.next = new_node
        self.tail = new_node
        return

    def insert_before(self, value, new_value, *args):
        current = self.head
        new_list = [new_value]+list(args)
        while current.next:
            if current.next.value == value:
                for arg in new_list:
                    new_node = Node(arg, current.next, current)
                    current.next.back = new_node
                    current.next = new_node
                    current = current.next
                return
            current = current.next

    def insert_after(self, value, new_value, *args):
        current = self.head
        new_list = [new_value]+list(args)
        while current.next:
            if current.value == value:
                for arg in new_list:
                    new_node = Node(arg, current.next, current)
                    current.next.back = new_node
                    current.next = new_node
                    current = new_node
                return
            current = current.next

    def delete_node(self,value):
        current = self.head
        while current.next:
            if current.next.value == value:
                deleted_node = current.next
                new_fragment = deleted_node.next
                current.next = new_fragment
                if deleted_node == self.tail:
                    self.tail = current
                else:
                    new_fragment.back = current
                deleted_node.back = None
                deleted_node.next = None
                return deleted_node
            current = current.next

    def kth_from_end(self, k):
        if k<0:
            return "Exception"
        counter = 0
        current = self.tail
        while current.back:
            if counter == k:
                return current.value
            counter += 1
            current = current.back
        return "Exception"


    def __str__(self):
        str = ""
        current = self.head
        while current:
            str += f"{{{current.value}}} <-->"
            current = current.next
        return f"{str} Null"

def ll_merge(ll1, ll2):
    ''' merges two doubly linked lists'''
    if not ll1.head and not ll2.head:
        return "no heads provided"
    elif not ll1.head and ll2.head:
        return ll2
    elif not ll2.head and ll1.head:
        return ll1
    current1, current2 = ll1.head, ll2.head
    while current2:
        fragment1 = current1.next
        current1.next, current2.back = current2, current1
        fragment2 = current2.next
        if fragment1:
            current1 = fragment1
        else:
            current1.next=current2
            current2.back = current1
            ll1.tail = ll2.tail
            break
        current2.next = fragment1
        current2 = fragment2
    return ll1

if __name__ == "__main__":
    ll = DoubleLinkedList()
    ll.add_node("apples")
    ll.add_node("oranges")
    ll.add_node("kiwi", "oranges", "grapes")
    ll.append("juice")
    ll.append("cranberry")
    ll.insert_before("juice", "insertbefore1", "test2", "test3")
    ll.insert_after("juice", "insertafter1","test4","test5" )
    ll.append("newtail")
    print(ll.delete_node("newtail"))
    print(ll.delete_node("cranberry"))
    print(ll)
    print(ll.kth_from_end(5))

