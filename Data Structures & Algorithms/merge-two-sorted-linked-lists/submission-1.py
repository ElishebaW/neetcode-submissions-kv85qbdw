# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        T: O(M+n) = where m = len(list1) and n =len(list2)
        S: O(1) = because I can reuse nodes when merging
        """

        dummyNode = ListNode(0)
        current = dummyNode

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        
        if list1 != None:
            current.next = list1
        if list2 != None:
            current.next = list2

        return dummyNode.next
            
        