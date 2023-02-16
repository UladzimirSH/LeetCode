class MyStack:

    def __init__(self):
        self.main_queue = []
        self.top_queue = []
        self.top_element = -1

    def push(self, x: int) -> None:
        self.main_queue.append(x)
        self.top_element = x

    def pop(self) -> int:
        while len(self.main_queue) > 1:
            self.top_element = self.main_queue.pop(0)
            self.top_queue.append(self.top_element)
        result = self.main_queue.pop(0)
        self.main_queue = self.top_queue
        self.top_queue = []
        return result

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return not self.main_queue and not self.top_queue


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.pop())
print(myStack.top())