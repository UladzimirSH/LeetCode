class MovingAverage:

    def __init__(self, size: int):
        self.array = [0] * size
        self.size = size
        self.current_sum = 0
        self.current_count = 0
        self.head = -1
        self.tail = -1

    def isFull(self) -> bool:
        return ((self.tail + 1) % self.size) == self.head

    def next(self, val: int) -> float:
        if self.head == -1:
            self.head = 0

        if self.current_count != self.size:
            self.current_count += 1

        self.tail = (self.tail + 1) % self.size
        if self.tail == self.head:
            # dequeue
            self.current_sum -= self.array[self.head]
            self.head = (self.head + 1) % self.size

        self.array[self.tail] = val
        self.current_sum += val

        return self.current_sum / self.current_count


movingAverage = MovingAverage(3);
print(movingAverage.next(1))  # return 1.0 = 1 / 1
print(movingAverage.next(10))  # return 5.5 = (1 + 10) / 2
print(movingAverage.next(3))  # return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5))  # return 6.0 = (10 + 3 + 5) / 3
