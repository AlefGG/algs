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