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

        if self.stack_to_dequeue.isEmpty():
            raise RuntimeError("cannot dequeue from empty queue")

        return self.stack_to_dequeue.pop()

    def __str__(self):
        """ { a } -> { b } -> { c } -> NULL """
        final_string = ""

        while not self.stack_to_dequeue.isEmpty():
            self.stack_to_enqueue.push(self.stack_to_dequeue.pop())

        current = self.stack_to_enqueue.top

        while current:
            final_string += f" <-- {{{current.value}}} "
            current = current.next

        return f"NULL{final_string}"


if __name__ == "__main__":
    pq = PseudoQueue()
    pq.dequeue()
    pq.enqueue("apples","oranges","grapefruit")
    pq.dequeue()
    pq.enqueue("coconuts", "mangoes")
    actual = str(pq)
    print(actual)


