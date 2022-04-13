def findCycleStart(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else: return None

    while slow != head:
        slow = slow.next
        head = head.next

    return head