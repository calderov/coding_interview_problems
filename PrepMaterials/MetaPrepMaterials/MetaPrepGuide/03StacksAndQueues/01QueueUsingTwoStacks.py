# Queue using Two Stacks
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

class Queue:
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def enqueue(self, val):
        self.pushStack.append(val)

    def dequeue(self):
        if not self.pushStack and not self.popStack:
            return None
        
        if self.popStack:
            return self.popStack.pop()
        
        while self.pushStack:
            self.popStack.append(self.pushStack.pop())

        return self.popStack.pop()

    def peek(self):
        if self.popStack:
            print(self.popStack[-1])
            return

        if self.pushStack:
            print(self.pushStack[0])
            return

        print("None")

if __name__ == "__main__":
    queue = Queue()

    print("Expected:")
    print(14)
    print(14)
    print()

    print("Output:")
    queue.enqueue(42)
    queue.dequeue()
    queue.enqueue(14)
    queue.peek()
    queue.enqueue(28)
    queue.peek()
    queue.enqueue(60)
    queue.enqueue(78)
    queue.dequeue()
    queue.dequeue()