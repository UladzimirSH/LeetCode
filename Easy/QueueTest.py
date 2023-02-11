import queue

some = queue.Queue

some.put()
some.put(2)
some.put(3)

for n in some:
    print(n)