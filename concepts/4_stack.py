class Stack:
    def __init__(self):
        self.items = []

if __name__ == "__main__":
    stack = Stack()

    stack.insert(10)
    stack.insert(20)
    stack.insert(30)

    stack.delete(100)

    stack.print_queue()
