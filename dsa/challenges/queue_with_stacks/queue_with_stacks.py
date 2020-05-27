from dsa.data_structures.stack_and_queues.stack_and_queues import Stack
class PseudoQueue:
    def __init__(self):
        self.stack_to_enqueue = Stack()
        self.stack_to_dequeue = Stack()

    def enqueue(self, new_val, *args):
        while not self.stack_to_dequeue.isEmpty():
            self.stack_to_enqueue.push(self.stack_to_dequeue.pop())
        self.stack_to_enqueue.push(new_val, *args)
        return

    def dequeue(self):
        while not self.stack_to_enqueue.isEmpty():
            self.stack_to_dequeue.push(self.stack_to_enqueue.pop())
        return self.stack_to_dequeue.pop()

    def __str__(self):
        """ { a } -> { b } -> { c } -> NULL """
        final_string = ""

        while not self.stack_to_dequeue.isEmpty():
            self.stack_to_enqueue.push(self.stack_to_dequeue.pop())

        current = self.stack_to_enqueue.top

        while current:
            final_string += f"{{{current.value}}} -> "
            current = current.next

        return f"{final_string}NULL"


if __name__ == "__main__":
    new_queue = PseudoQueue()
    print(new_queue)
    new_queue.enqueue("apples", "oranges", "kiwi")
    print(new_queue)
    new_queue.stack_to_dequeue.push("3","2","1")
    print("this is new queue", new_queue)
    new_queue.enqueue("coconuts")
    print(new_queue.dequeue())
    print(new_queue)
    print(new_queue.dequeue())
    print(new_queue)
    print(new_queue.enqueue("grapefruit"))
    print(new_queue)


