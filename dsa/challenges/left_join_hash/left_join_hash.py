from dsa.challenges.hashtable.hashtable import Hashtable
from dsa.challenges.hashtable.linked_list_hashtable import LinkedList, Node

def left_join_hashtable(table1, table2):
    print("this si table1", table1)
    print("this is table2", table2)
    #iterate over the table1
    def walk(root_node):
        kv_pair = root_node.value
        root_node = kv_pair.append("NULL")
        return
    for i in range(len(table1.indices)):
        #check for match in table2 at these spots
        if table1.indices[i] and table2.indices[i]:
            print(table1.indices[i],table2.indices[i])

        elif table1.indices[i]:
            current = table1.indices[i].head
            while current:
                walk(current)
                current = current.next
            print("this is new LL", table1.indices[i])
            print(table1)

            #iterate over the linkedlist
            #grab the key,value of the node
            #change it to key,value,Null
            #do it for all the nodes at that index




if __name__ == "__main__":
    table1 = Hashtable(10)
    table2 = Hashtable(10)
    table1.add("JB",27)
    table1.add("Vij",32)
    table1.add("jiV", 22)
    table2.add("JB", 55)
    table2.add("Coreys",12)
    left_join_hashtable(table1, table2)
