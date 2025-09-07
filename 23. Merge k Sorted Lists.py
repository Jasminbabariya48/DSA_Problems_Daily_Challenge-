import heapq
from typing import List, Optional
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Initialize the heap with the head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next
    
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    # Creating k sorted linked lists for demonstration
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    
    lists = [list1, list2, list3]
    
    merged_head = solution.mergeKLists(lists)
    
    # Print merged linked list
    current = merged_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")