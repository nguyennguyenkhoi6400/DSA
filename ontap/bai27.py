class Queue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    def them(self, value):

        self.stack1.append(value)

    def xoa(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


queue = Queue()

queue.them(1)
queue.them(2)

print(queue.xoa())