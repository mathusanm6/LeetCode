from problems.easy.linked_list_cycle import Solution, ListNode


def test_linked_list_cycle():
    solution = Solution

    # Testcase 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    assert solution.hasCycle(solution, head)

    # Testcase 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert solution.hasCycle(solution, head)

    # Testcase 3
    head = ListNode(1)
    assert not solution.hasCycle(solution, head)

    # Testcase 4
    head = None
    assert not solution.hasCycle(solution, head)
