from dsa.data_structures.linked_list.linked_list import LinkedList, Node
from dsa.data_structures.stack_and_queues.stack_and_queues import Stack

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


#### note try this code with a list instead of a linked list

#### try with modifying it in the same list with O(n) time, but space O(1)
def partition (ll, value):
    # make a new linked list with a tail to hold high values and head to hold the small values
    # O(n) time but O(n) for space for new linked list
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

def new_sum_ll(ll_1, ll_2):
    #convert the ll_1 and ll_2 into a string and then into an integer
    if not ll_2.head:
        return ll_1
    elif not ll_1.head:
        return ll_2
    def to_integer(ll):
        string = ""
        current = ll.head
        while current:
            string+=str(current.value)
            current = current.next
        return int(string)
    def to_ll(num):
        new_ll = LinkedList()
        for n in str(num):
            new_ll.append(int(n))
        return new_ll
    sum = to_integer(ll_1)+to_integer(ll_2)
    return (to_ll(sum))

#### 2.6 function to check if linked list is a palindrome
def is_palindrome(ll):
    mid = ll.head
    scout = ll.head
    pal = Stack()
    # get the stack set up
    while scout.next:
        pal.push(mid.value)
        if scout.next.next:
            scout = scout.next.next
            mid = mid.next
        else:
            break
    mid = mid.next
    while mid:
        if mid.value == pal.peek():
            pal.pop()
            mid = mid.next
        else:
            return False
    return True

#### 2.7 function to find the intersection of two linked lists

def find_intersection1 (ll1, ll2):
    if not ll1.head or not ll2.head:
        return 'No intersection'
    node_list = []
    current = ll1.head
    while current:
        node_list.append(current.value)
        current = current.next
    current = ll2.head
    the_node = None
    switch = False
    pos = None
    while current:
        if current.value in node_list and switch == False:
            the_node = current
            pos = node_list.index(current.value)
            switch = True
        elif switch == True:
            pos += 1
            if pos>=len(node_list):
                return "no intersection"
            elif current.value != node_list[pos]:
                switch = False
        current = current.next
    if pos == len(node_list)-1 and switch == True:
        return the_node
    return "no intersection"

#another method from the textbook to find the intersection by first finding the shorter of the linked lists and as well as the tail and making sure the tails match
def find_intersection2(ll1, ll2):
    if not ll1.head or not ll2.head:
        return 'No intersection since no heads found'
    def find_tail_length(ll):
        current = ll.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        print(current,length)
        return current,length
    ll1_tail, ll1_len = find_tail_length(ll1)
    ll2_tail, ll2_len = find_tail_length(ll2)

    #check if the tails match in value.  If so, then they intersect or else they do not.
    if ll1_tail.value != ll2_tail.value:
        return "No intersection since tails do not match"
    if ll1_len<ll2_len:
        shorter, longer = ll1, ll2
    else:
        shorter, longer = ll2, ll1
    diff = abs(ll2_len-ll1_len)

    # adjust the longer of the linked lists to start it exactly same length as the shorter LL
    def adjust_longer(ll, diff):
        current = ll.head
        k = 0
        while k!=diff:
            current = current.next
            k +=1
        ll.head = current
        return ll
    longer = adjust_longer(longer,diff)
    
    #traverse through the linked lists to find the intersection
    current_s, current_l = shorter.head, longer.head
    while current_s:
        if current_s.value == current_l.value:
            return current_s
        current_s, current_l = current_s.next, current_l.next
    return "no intersection"


if __name__ == "__main__":
    ll_1 = LinkedList()
    ll_2 = LinkedList()
    # ll = LinkedList()
    # ll.insert("A", "B", "C", "C", "B", "D")
    # print(ll)
    # ll.insert("C", "E", "A", "E", "D", "C", "A", "C", "A")
    # print(delete_middle(ll))
    # ll.insert(1, 2, 8, 3, 5, -1,200)
    # print("this is the ll", ll)
    # print(partition(ll, 3))
    ll_1.append(1,2,3,11)
    ll_2.append(5,25, 45, 22,3,11)
    print("One", ll_1, "Two", ll_2)
    # # print(sum_lists(ll_1, ll_2))
    # print(sum_lists2(ll_1, ll_2))
    # print(new_sum_ll(ll_1, ll_2))
    print(find_intersection2(ll_1, ll_2))



