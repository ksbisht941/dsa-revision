class Queue:
    def __init__(self):
        """Initialize an empty queue backed by a Python list."""
        self._items = []

    def is_empty(self):
        """Return True if the queue contains no elements."""
        return len(self._items) == 0

    def enqueue(self, value):
        """Add a value to the rear of the queue."""
        self._items.append(value)

    def enqueue_front(self, value):
        """Add a value to the front of the queue."""
        self._items.insert(0, value)

    def dequeue(self):
        """Remove and return the value from the front of the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)

    def dequeue_rear(self):
        """Remove and return the value from the rear of the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from the rear of an empty queue")
        return self._items.pop()

    def peek_front(self):
        """Return the value at the front without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue")
        return self._items[0]

    def peek_rear(self):
        """Return the value at the rear without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue")
        return self._items[-1]

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._items)

    def display(self):
        """Print the queue contents from front to rear."""
        print(self._items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    queue.enqueue_front(5)
    queue.enqueue_front(0)

    print("Front of queue:", queue.peek_front())
    print("Rear of queue:", queue.peek_rear())
    print("Queue length:", len(queue))

    removed_front = queue.dequeue()
    print("Removed from front:", removed_front)

    removed_rear = queue.dequeue_rear()
    print("Removed from rear:", removed_rear)

    queue.display()
