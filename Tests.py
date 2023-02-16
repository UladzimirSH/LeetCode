import queue


class Tests:

    def queue_test(self):
        some = []
        some.append(1)
        some.append(2)
        some.append(3)

        print(some)
        some.pop()
        print(some)
        some.pop(0)
        print(some)

solution = Tests()
solution.queue_test()
