class Queue:
    
    def __init__(self):
        
        self.queue = []
        
    def them(self, value):

        self.queue.append(value)

    def xoa(self):

        if self.queue:
            return self.queue.pop(0)

    def rong(self):

        return len(self.queue) == 0


queue = Queue()

queue.them(10)
queue.them(20)

print(queue.xoa())