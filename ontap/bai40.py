def sap_xep(head):

    array = []

    while head:

        array.append(head.value)
        head = head.next

    array.sort()

    return array