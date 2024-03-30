class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")
    def show(self):
        return self.queue.copy()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())
print("Front element:", queue.peek())

while not queue.is_empty():
    print("Dequeued:", queue.dequeue())

print("size of the queue", queue.size())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("size of the queue", queue.size())
print("queue elements", queue.show())
