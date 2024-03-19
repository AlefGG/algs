from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def toString(self, list: ListNode):
        res = []
        while list:
            res.append(list.val)
            list = list.next
        print(res)

    def createLinkedListFromArray(self, lst: list) -> ListNode:
        head = ListNode() 
        curr = head

        for val in lst:
            curr.next = ListNode(val)  
            curr = curr.next  
        return head.next 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        list3 = head
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            elif list1.val > list2.val:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next 
        if not list2:
            while list1:
                list3.next = list1
                list3 = list3.next 
                list1 = list1.next
        if not list1:
            while list2:
                list3.next = list2
                list3 = list3.next 
                list2 = list2.next
        return head.next



linkedList = LinkedList()
sol = Solution()
l1 = linkedList.createLinkedListFromArray([1,2,4])
l2 = linkedList.createLinkedListFromArray([1,3,4])
linkedList.toString(l1)
linkedList.toString(l2)
l3 = sol.mergeTwoLists(l1, l2)
linkedList.toString(l3)
