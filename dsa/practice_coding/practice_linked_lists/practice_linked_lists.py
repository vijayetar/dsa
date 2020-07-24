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

# 2.5
def sum_lists(ll_1, ll_2):
    if not ll_1.head or not ll_2.head:
        return "ll does not have head"
    ll= LinkedList()
    current_1 = ll_1.head
    current_2 = ll_2.head
    carry_over = 0
    while current_1 and current_2:
        sum = current_1.value + current_2.value + carry_over
        if sum>9:
            new_value = sum-10
            carry_over = 1
        else:
            new_value = sum
            carry_over = 0
        if not ll.head:
            ll.head=Node(new_value)
            ll.tail = ll.head
        else:
            ll.tail.next = Node(new_value)
            ll.tail= ll.tail.next
        current_1=current_1.next
        current_2=current_2.next
    while current_1:
        sum = current_1.value + carry_over
        if sum>9:
            new_value = sum-10
            carry_over = 1
        else:
            new_value = sum
            carry_over = 0
        ll.tail.next = Node(new_value)
        ll.tail= ll.tail.next
        current_1 = current_1.next
    while current_2:
        sum = current_2.value + carry_over
        if sum>9:
            new_value = sum-10
            carry_over = 1
        else:
            new_value = sum
            carry_over = 0
        ll.tail.next = Node(new_value)
        ll.tail= ll.tail.next
        current_2 = current_2.next
    if carry_over:
        ll.tail.next = Node(carry_over)
        ll.tail= ll.tail.next
    return ll

#2.5 refactored
def sum_lists2(ll_1, ll_2):
    if not ll_1.head or not ll_2.head:
        return "ll does not have head"
    ll= LinkedList()
    current_1 = ll_1.head
    current_2 = ll_2.head
    carry_over = 0

    def get_new_value(sum,carry_over):
        if sum>9:
            new_value = sum-10
            carry_over = 1
        else:
            new_value = sum
            carry_over = 0
        return new_value, carry_over

    def add_to_tail(new_value):
        ll.tail.next = Node(new_value)
        ll.tail= ll.tail.next

    while current_1 and current_2:
        sum = current_1.value + current_2.value + carry_over
        new_value, carry_over = get_new_value(sum, carry_over)
        if not ll.head:
            ll.head=Node(new_value)
            ll.tail = ll.head
        else:
            add_to_tail(new_value)
        current_1=current_1.next
        current_2=current_2.next
    if current_1:
        remaining = current_1
    else:
        remaining = current_2
    while remaining:
        sum = remaining.value + carry_over
        new_value, carry_over = get_new_value(sum, carry_over)
        add_to_tail(new_value)
        remaining = remaining.next
    if carry_over:
        ll.tail.next = Node(carry_over)
        ll.tail= ll.tail.next
    return ll


if __name__ == "__main__":
    ll_1 = LinkedList()
    ll_2 = LinkedList()
    # ll.insert("A", "B")
    # ll.insert("C", "E", "A", "E", "D", "C", "A", "C", "A")
    # print(delete_middle(ll))
    # ll.insert(1, 2, 8, 3, 5, -1,200)
    # print("this is the ll", ll)
    # print(partition(ll, 3))
    ll_2.insert(9,9,9,9)
    ll_1.insert(9,9,9,9,9)
    print(sum_lists(ll_1, ll_2))
    print(sum_lists2(ll_1, ll_2))



