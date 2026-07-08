class Node:

    def __init__(self, value):

        self.value = value
        self.next = None


def dao_nguoc(head):

    prev = None

    while head:

        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev