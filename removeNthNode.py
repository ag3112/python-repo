#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cNode = head
        pNone = None
        while True:
            if cNode.next is None:
                pNode.next = cNode
                break
            else:
                pNode = cNode
                cNode = cNode.next

        return head




if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = ListNode(5)

    print(l.val)
    print(l.next.val)
    print(l.next.next.val)
    print(l.next.next.next.val)
    print(l.next.next.next.next.val)


    s = Solution()
    l = s.removeNthFromEnd(l, 2)

    print(l.val)
    print(l.next.val)
    print(l.next.next.val)
    print(l.next.next.next.val)
    print(l.next.next.next.next.val)

