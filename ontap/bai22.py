class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = []

    def them(self, value):

        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def xoa(self):

        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def lay_nho_nhat(self):

        return self.min_stack[-1]


stack = MinStack()

stack.them(5)
stack.them(2)
stack.them(7)

print(stack.lay_nho_nhat())