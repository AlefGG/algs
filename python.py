class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next:
            self.tail = new

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(index):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return
            else:
                new_node = ListNode(val)
                new_node.next = curr.next
                curr.next = new_node
                if new_node.next is None:
                    self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)