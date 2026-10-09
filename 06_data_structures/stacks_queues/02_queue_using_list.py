# File: 06_data_structures/stacks_queues/02_queue_using_list.py

class Queue:
    """Queue implementation using a Python list (FIFO)."""

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        return self._items.pop(0)

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue.")

        return self._items[0]

    def is_empty(self):
        """Return True if the queue has no elements."""
        return len(self._items) == 0

    def size(self):
        """Return the number of elements."""
        return len(self._items)

    def display(self):
        """Display elements from front to rear."""
        print(self._items)


if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue:")
    queue.display()

    print("Front element:", queue.peek())
    print("Queue size:", queue.size())

    print("Dequeued:", queue.dequeue())

    print("Updated queue:")
    queue.display()

    print("Is empty?", queue.is_empty())