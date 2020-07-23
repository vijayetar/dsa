from dsa.data_structures.linked_list.linked_list import LinkedList, Node

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

# 2.3 find the middle node
def find_middle(ll):
    print(ll)
    if not ll:
        return "no linked list provided"
    if not ll.head.next:
        return ll.head.value
    current = ll.head
    mid = current
    while current.next:
        if current.next.next:
            current = current.next.next
            mid = mid.next
        else:
            break
    return mid.value

# 2.3a find and remove the middle node
def delete_middle(ll):
    if not ll:
        return "no linked list provided"
    current = ll.head
    mid = current
    prev = current
    while current.next:
        if current.next.next:
            current = current.next.next
            mid = mid.next
            if prev.next != mid:
                prev = prev.next
        else:
            break
    prev.next = mid.next
    mid.next = None
    return ll

# 2.4 given ll and value, partition ll on that value
## assumptions only integers given, including negative values,  no characters given.  and value present in the linked list

def partition (ll, value):
    # make a new linked list with a tail to hold high values and head to hold the small values
    output_ll = LinkedList()
    output_ll.tail = output_ll.head
    current = ll.head
    while current:
        if current.value < value:
            if not output_ll.head:
                output_ll.head = Node(current.value)
                output_ll.tail = output_ll.head
            else:
                new_node = Node(current.value)
                new_node.next = output_ll.head
                output_ll.head = new_node
        else:
            #add to the tail
            if not output_ll.tail:
                output_ll.tail = Node(current.value)
                output_ll.head = output_ll.tail
            else:
                new_node = Node(current.value)
                output_ll.tail.next = new_node
                output_ll.tail = new_node
        current = current.next
    return output_ll




if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert("A", "B")
    # ll.insert("C", "E", "A", "E", "D", "C", "A", "C", "A")
    # print(delete_middle(ll))
    ll.insert(1, 2, 8, 3, 5, -1,200)
    print("this is the ll", ll)
    print(partition(ll, 3))



