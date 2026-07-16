# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res1,res2=[],[]

        #save the list in array
        while l1 or l2 :
            if l1:
                res1.append(l1.val)
                l1=l1.next
            if l2:
                res2.append(l2.val)
                l2=l2.next

        # rever the array
        res1.reverse()
        res2.reverse()

        # construct a number out of both array
        result=0
        for digit in res1:
            result = result * 10+ digit
        result1=0
        for digit in res2:
            result1 = result1*10+ digit
        ans=result+result1

        if ans== 0:
            return ListNode(0)

        # reverse the added number and convert it ot a list
        n = ans
        new_array = []
        while n:
            digit = n % 10
            new_array.append(digit)
            n = n // 10
        new_array
 
        #convert the array to a list

        newnode= ListNode()
        temp=newnode
        for i in new_array:
            newnode.next= ListNode(i)
             
            newnode=newnode.next
        newnode.next=None
        return temp.next










        