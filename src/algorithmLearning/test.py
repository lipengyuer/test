import time
import copy

class ListNode():
    def __init__(self, v):
        self.val = v
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
      """
        res1, res2 = addTwoNode(l1.val, l2.val)

        resNodes = ListNode(res2)
        resNodes.next = None
        if res1 == 0 and res2 == 0 and l1.next == None and l2.next == None:
            return reverseNodeList(resNodes)
        H = res1

        l1 = copy.deepcopy(l1.next)
        l2 = copy.deepcopy(l2.next)
        count = 0
        t1 = time.time()
        while True:
            if l1 == None and l2 == None and res1 == 0 and H == 0:
                break
            count += 1
            res1, res2 = addTwoNode(l1.val if l1 else None, l2.val if l2 else None)
            TR = H + res2
            if TR >= 10:
                resNodesTemp = ListNode(TR % 10)
                H = TR // 10
            else:
                resNodesTemp = ListNode(TR)
                H = res1
            resNodesTemp.next = resNodes  # copy.deepcopy(resNodes)
            resNodes = copy.deepcopy(resNodesTemp)
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        t2 = time.time()

        res = reverseNodeList(resNodes)
        t3 = time.time()
        #         print("时间", t2-t1, t3-t2)

        return res


def addTwoNode(N1, N2):
    n1 = 0
    n2 = 0
    if N1 == None and N2 != None:
        n2 = N2
    if N1 != None and N2 == None:
        n1 = N1
    if N1 != None and N2 != None:
        n2 = N2
        n1 = N1
    res = n1 + n2
    if res >= 10:
        return res // 10, res % 10
    else:
        return 0, res


def reverseNodeList(nodeList):
    resNodes = ListNode(nodeList.val)
    resNodes.next = None
    while nodeList.next != None:
        nodeList = nodeList.next
        tempNode = copy.deepcopy(resNodes)
        resNodes.val = nodeList.val
        resNodes.next = tempNode
    return resNodes

if __name__ == '__main__':
    n1 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
     9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
     9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    n2 = [1]