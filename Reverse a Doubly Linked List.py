from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            if node:
                node.prev = head
            node = head
            head = temp
        return node
    
if __name__ == "__main__":
    # Create a doubly linked list: 1 <-> 2 <-> 3
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    head.next = second
    head.prev = None
    second.next = third
    second.prev = head
    third.next = None
    third.prev = second

    # Reverse the doubly linked list
    solution = Solution()
    new_head = solution.reverseList(head)

    # Print the reversed list
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next