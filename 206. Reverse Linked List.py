from typing import Optional


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        stack = []
        temp = head
        
        while temp.next is not None:
            stack.append(temp)
            temp = temp.next
            
        head = temp
            
        while stack:
            temp.next = stack.pop()
            temp = temp.next
            
        temp.next = None
        
        return head
    
if __name__ == "__main__":
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    new_head = sol.reverseList(head)
    
    temp = new_head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")