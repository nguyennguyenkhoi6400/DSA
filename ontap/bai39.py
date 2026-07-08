class Node:

    def __init__(self, value):

        self.value = value
        self.next = None


def xoa_tu_cuoi(head, k):

    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(k):

        if fast.next is None:
            return head

        fast = fast.next

    while fast.next:

        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


def hien_thi(head):

    while head:

        print(head.value, end=" ")

        head = head.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = xoa_tu_cuoi(head, 2)

hien_thi(head)