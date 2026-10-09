
class Stack:
    """Stack implementation using a Python list (LIFO)."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an element to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self._items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack.")

        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no elements."""
        return len(self._items) == 0

    def size(self):
        """Return the number of elements."""
        return len(self._items)

    def display(self):
        """Display elements from bottom to top."""
        print(self._items)


if __name__ == "__main__":
    stack = Stack()

    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:")
    stack.display()

    print("Top element:", stack.peek())
    print("Stack size:", stack.size())

    print("Popped:", stack.pop())

    print("Updated stack:")
    stack.display()

    print("Is empty?", stack.is_empty())