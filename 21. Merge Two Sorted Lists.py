from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        head = None
        while list1 != None and list2!= None:
            val = 0
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            
            if not head:
                head = ListNode(val)
                newList = head
            else:
                newList.next = ListNode(val)
                newList = newList.next
        
        if list1 == None:
            head = self.createNodes(head,newList,list2)
        elif list2 == None:
            head = self.createNodes(head,newList,list1)
        
        return head

    def createNodes(self, head,newList,listItem):
        while listItem != None:
            val = listItem.val
            if not head:
                head = ListNode(val)
                newList = head
            else:
                newList.next = ListNode(val)
                newList = newList.next
            listItem = listItem.next
        return head

    def display(self, listNode):
        while listNode != None:
            print(listNode.val,'->',end='')
            listNode = listNode.next
        print()
    
def makeLinkList(arr):
    newList = None
    head = None

    for val in arr:
        if not head:
            head = ListNode(val)
            newList = head
        else:
            newList.next = ListNode(val)
            newList = newList.next 
    return head

list1 = makeLinkList([1,2,4,5])
list2 = makeLinkList([1,4,5,6])

sol = Solution()
sol.display(list1)
sol.display(list2)

newlist = sol.mergeTwoLists(list1,list2)

sol.display(newlist)