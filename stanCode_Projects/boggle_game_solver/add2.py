"""
File: add2.py
Name: Johnson
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # To avoid considering the head node
    dummy = ListNode(0)
    node = dummy

    # when adding two number and the answer over 10, we will modulate the carry to get multiple number adding answer
    carry = 0

    # Using or to control the situation that length of l1 is not equal to l2
    # For example: if l1 is shorter, l1.val will be set as 0, and we will adding l2.val with l1=0
    # after adding process, we will let l1 node still at l1, and l2 will become l2.next
    while l1 is not None or l2 is not None:
        if l1 is not None:
            l1_val = l1.val
            l1 = l1.next
        else:
            l1_val = 0
            l1 = l1
        if l2 is not None:
            l2_val = l2.val
            l2 = l2.next
        else:
            l2_val = 0
            l2 = l2

        # make the node.next become the answer of unit digit
        node.next = ListNode((l1_val + l2_val + carry) % 10)

        # when the answer of d1+d2 over 10, we use carry to store the tens digit
        carry = (l1_val + l2_val + carry) // 10
        node = node.next

        # if while loop is break but there still have carry, we will create a new node which value is carry
        if carry != 0:
            node.next = ListNode(carry)

    # ignore the dummy node, so we return dummy.next
    return dummy.next


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
