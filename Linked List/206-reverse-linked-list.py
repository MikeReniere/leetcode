# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            print(head.val)

        return 0

test = Solution
print('aaa')
head = [1,2,3,4,5]
print(test.reverseList())