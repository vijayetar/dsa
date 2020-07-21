from dsa.data_structures.linked_list.linked_list import LinkedList

#### 2.1 Remove Duplicates from unsorted linked list.  Implement it with and without a temporary buffer

#with a temporary buffer

def remove_duplicates(ll):
    print(ll)
    if not ll:
        return "no linked list provided"
    if not ll.head.next:
        return ll
    nodes = []
    prev = ll.head
    nodes.append(prev.value)
    current = prev.next
    while prev.next:
        if current.value not in nodes:
            nodes.append(current.value)
            prev = prev.next
            current = current.next
        else:
            prev.next = current.next
            current.next = None
            current = prev.next
    return ll



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert("D", "C", "A", "C", "A")
    print(remove_duplicates(ll))

