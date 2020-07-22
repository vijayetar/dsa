from dsa.data_structures.linked_list.linked_list import LinkedList

#### 2.1 Remove Duplicates from unsorted linked list.  Implement it with and without a temporary buffer

#with a temporary buffer
def remove_duplicates(ll):
    print(ll)
    if not ll:
        return "no linked list provided"
    if not ll.head.next:
        return ll
    nodes = {}
    prev = ll.head
    nodes[prev.value]= True
    current = prev.next
    while prev.next:
        if current.value not in nodes:
            nodes[current.value]=True
            prev = prev.next
            current = current.next
        else:
            prev.next = current.next
            current.next = None
            current = prev.next
    return ll

#without temporary buffer
def remove_duplicates2(ll):
    print(ll)
    if not ll:
        return "no linked list provided"
    if not ll.head.next:
        return ll
    current = ll.head
    while current:
        prev = current
        runner = current.next
        while runner:
            if runner.value == current.value:
                prev.next = runner.next
                runner = runner.next
            else:
                prev = prev.next
                runner = runner.next
        current = current.next
    return ll


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert("C", "E", "A", "E", "D", "C", "A", "C", "A")
    print(remove_duplicates2(ll))

