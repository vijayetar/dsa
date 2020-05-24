from dsa.data_structures.linked_list.linked_list import Node, LinkedList

def merge_list(link1, link2):
        scout1 = link1.head
        scout2 = link2.head
        if not scout1 and scout2:
            scout1 = scout2
            return scout1
        elif not scout2 and scout1:
            return scout1
        switch = True
        while switch:
                current1 = scout1
                current2 = scout2
                scout1 = scout1.next
                scout2 = scout2.next
                if not scout1 or not scout2:
                        switch = False
                current1.next = current2
                current2.next = scout1
        if scout2 != None:
                current2.next = scout2
        return link1.head

if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert("a","b")
    ll2.insert("a","b","c","d","e","f")
    print(merge_list(ll1, ll2))

