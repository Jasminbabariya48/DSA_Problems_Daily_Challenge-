from typing import Optional

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def findlen(self, slow, fast):
        cnt = 1
        fast = fast.next
        
        
        while slow != fast:
            cnt += 1
            fast = fast.next
            
        return cnt


    def lengthOfLoop(self, head: Optional[Node]) -> int:
        slow = head
        fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return self.findlen(slow, fast)
                
        return 0
    
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    # Creating a linked list with a loop for demonstration
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # Creating a loop here
    head.next.next.next.next.next = head.next  # Loop starts at node with value 2

    result = solution.lengthOfLoop(head)
    print(f"The length of the loop is: {result}")