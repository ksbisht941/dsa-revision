class CircularQueue:
    def __init__(self, size):
        """Initialize the circular queue with a fixed capacity."""
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """Return True when the queue has no elements."""
        return self.front == -1

    def is_full(self):
        """Return True when the queue is full and cannot accept new elements."""
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        """Add a value to the rear of the circular queue."""
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            # First element inserted.
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value

    def dequeue(self):
        """Remove and return the value at the front of the queue."""
        if self.is_empty():
            print("Queue is empty")
            return None

        value = self.items[self.front]

        if self.front == self.rear:
            # Queue becomes empty after removing the last element.
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(value)
        return value

    def display(self):
        """Print queue elements from front to rear."""
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.front
        values = []

        while True:
            values.append(self.items[current])
            if current == self.rear:
                break
            current = (current + 1) % self.size

        print(values)


if __name__ == "__main__":
    circularQueue = CircularQueue(5)

    circularQueue.enqueue(10)
    circularQueue.enqueue(20)
    circularQueue.enqueue(30)
    circularQueue.enqueue(40)
    circularQueue.enqueue(50)

    circularQueue.dequeue()
    circularQueue.dequeue()
    circularQueue.dequeue()

    circularQueue.display()
