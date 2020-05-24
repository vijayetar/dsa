from dsa.data_structures.linked_list.linked_list import Node, LinkedList

def reverse_link(link1):
    if not link1.head:
        return "No values in linked list"
    current = link1.head
    if not current.next:
        return link1
    next_value = current.next
    if not next_value.next:
        current.next = next_value.next
        next_value.next = current
        link1.head = next_value
        return link1
    current = next_value
    next_value = next_value.next
    previous = link1.head
    previous.next = None
    while next_value.next != None:
        current.next, previous, current, next_value = previous, current, next_value, next_value.next
    current.next, next_value.next = previous, current
    link1.head = next_value
    return link1

def check_palindrome(link1):
    link1_list = []
    current = link1.head
    while current:
        link1_list.append(current.value)
        current= current.next
    mid = int(len(link1_list)/2)
    n = -1
    for i in range(mid):
        print(i)
        if link1_list[i] == link1_list[n]:
            n = n-1
        else:
            return False
    return True

if __name__ == "__main__":
    ll = LinkedList()
    print(reverse_link(ll))
    ll.insert("apples")
    print(reverse_link(ll))
    ll.insert("bananas")
    print("this is ll:  ",ll)
    print(reverse_link(ll))
    ll.insert("carrots","kiwi","coconuts")
    pl = LinkedList()
    pl.insert("1","2","3","2","1")
    print("this is pl:  ",pl)
    print(check_palindrome(pl))
    print(check_palindrome(ll))
