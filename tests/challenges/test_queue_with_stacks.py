import pytest
from dsa.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_pseudoqueue():
    assert PseudoQueue()

def test_pseudoqueue_initiate_empty_queue():
    pq = PseudoQueue()
    actual = str(pq)
    expected = "NULL"
    assert actual == expected

def test_pseudoqueue_enqueue():
    pq = PseudoQueue()
    pq.enqueue("apples","oranges","grapefruit")
    actual = str(pq)
    expected = "NULL <-- {grapefruit}  <-- {oranges}  <-- {apples} "
    assert actual == expected

def test_pseudoqueue_dequeque():
    pq = PseudoQueue()
    pq.enqueue("apples","oranges","grapefruit")
    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected

def test_pseudoqueue_dequeque_enqueue():
    pq = PseudoQueue()
    pq.enqueue("apples","oranges","grapefruit")
    pq.dequeue()
    pq.enqueue("coconuts", "mangoes")
    actual = str(pq)
    expected = "NULL <-- {mangoes}  <-- {coconuts}  <-- {grapefruit}  <-- {oranges} "
    assert actual == expected

def test_pseudoqueue_dequeque_to_empty():
    pq = PseudoQueue()
    pq.enqueue("apples","oranges","grapefruit")
    pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    actual = str(pq)
    expected = "NULL"
    assert actual == expected

def test_pseudoqueue_dequeque_raiseError():
    pq = PseudoQueue()
    with pytest.raises(RuntimeError):
        pq.dequeue()

