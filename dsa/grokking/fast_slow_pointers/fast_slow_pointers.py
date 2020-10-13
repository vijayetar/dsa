from dsa.data_structures.linked_list.linked_list import LinkedList

# 3.1 Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

def find_happy_number(num):
    product_set = set()
    sum= _get_product(num, product_set)
    if sum==1:
        return True
    else:
        return False

def _get_product(num, product_set):
    sum = _find_sum_of_squares(num)
    if sum==1:
        return 1
    if sum not in product_set:
        product_set.add(sum)
        sum = _get_product(sum, product_set)
        return sum
    else:
        return 0

def _find_sum_of_squares(num):
    num_str = str(num)
    sum = 0
    for char in num_str:
        sum += int(char)**2
    return sum

# 3.2 Linked Lists
# def reorder(head):
#     if not head:
#         return "No linked List"
#     slow = head
#     fast = head

#     while (fast is not None and fast.next is not None):

#         slow = slow.next
#         fast = fast.next.next

#     current = head
#     while True:
#         current.next =


#     def _flip_nodes(current):
#         _prev = None
#         while current:
#             _temp = current.next
#             current.next = _prev
#             _prev = current
#             current = _temp
#         return _prev




#     return slow.value


# 3.3 Reverse a linkedList in place

def reverse(head):
    if not head:
        return "no linked list provided"
    current = head
    prev = None
    # while current.next:






if __name__ == "__main__":
#   print(find_happy_number(23))
#   print(find_happy_number(12))
  ll = LinkedList()
  ll.insert(1,2,3,4,5,6)
  print(reverse(ll))
