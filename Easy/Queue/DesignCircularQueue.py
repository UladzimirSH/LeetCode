class MyCircularQueue:

    def __init__(self, k: int):
        self.array = [-1] * k
        self.tail = -1
        self.head = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail + 1) % self.size

        self.array[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.tail == self.head:
            self.tail = -1
            self.head = -1
            return True

        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return ((self.tail + 1) % self.size) == self.head


#self.array[(self.head + 1) % self.size] != -1
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # return True
print(myCircularQueue.enQueue(2))  # return True
print(myCircularQueue.enQueue(3))  # return True
print(myCircularQueue.enQueue(4))  # return False
print(myCircularQueue.Rear())  # return 3
print(myCircularQueue.isFull())  # return True
print(myCircularQueue.deQueue())  # return True
print(myCircularQueue.enQueue(4))  # return True
print(myCircularQueue.Rear())  # return 4
