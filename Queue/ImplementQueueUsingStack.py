class MyQueue:

    def __init__(self):
        self.current_stack = []
        self.top_stack = []

    def push(self, x: int) -> None:
        self.current_stack.append(x)

    def pop(self) -> int:
        if self.top_stack:
            return self.top_stack.pop()

        while self.current_stack:
            self.top_stack.append(self.current_stack.pop())

        return self.top_stack.pop()

    def peek(self) -> int:
        if self.top_stack:
            return self.top_stack[-1]

        while self.current_stack:
            self.top_stack.append(self.current_stack.pop())

        return self.top_stack[-1]

    def empty(self) -> bool:
        return not self.current_stack and not self.top_stack


myQueue = MyQueue()
print(myQueue.push(1)) # queue is: [1]
print(myQueue.push(2)) # queue is: [1, 2]
print(myQueue.push(3)) # queue is: [1, 2, 3]
print(myQueue.pop())
print(myQueue.push(4)) # queue is: [2, 3, 4]
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.empty()) # return true