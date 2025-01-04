# 1st Solution - Using Lists and Conversion
# This approach uses lists to handle operations and conversions to and from linked lists.
# - Converts the linked lists into Python lists.
# - Adds corresponding digits with carry handling.
# - Converts the result list back into a linked list.
# - Time Complexity: O(n), where n is the length of the longer list.
# - Space Complexity: O(n), due to the use of intermediate lists.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []  # Using a list to store results
        carry = 0  # Initialize carry to 0

        # Helper function to convert a linked list to a Python list
        def linked_list_to_list(node: ListNode) -> list:
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        # Helper function to convert a Python list to a linked list
        def list_to_linked_list(lst: list) -> Optional[ListNode]:
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for num in lst[1:]:
                current.next = ListNode(num)
                current = current.next
            return head

        # Convert input linked lists to Python lists
        l1_list = linked_list_to_list(l1)
        l2_list = linked_list_to_list(l2)

        # Ensure l1_list is the longer list, pad the shorter one with zeroes
        if len(l1_list) < len(l2_list):
            l1_list, l2_list = l2_list, l1_list
        l2_list += [0] * (len(l1_list) - len(l2_list))

        # Add digits with carry handling
        for i in range(len(l1_list)):
            abc = l1_list[i] + l2_list[i] + carry
            if abc >= 10:
                carry = 1
                abc = abc % 10
            else:
                carry = 0
            answer.append(abc)

        # If there's a remaining carry, add it to the result
        if carry:
            answer.append(carry)

        # Convert result list back to a linked list
        return list_to_linked_list(answer)

# 2nd Solution - Iterative with Constant Space
# This approach uses an iterative method without extra space for lists.
# - Traverses both linked lists simultaneously.
# - Adds corresponding digits with carry handling directly.
# - Constructs the result as a new linked list.
# - Time Complexity: O(n), where n is the length of the longer list.
# - Space Complexity: O(1), only the result linked list takes extra space.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)  # Dummy node to simplify result list construction
        current, carry = dummy, 0

        while l1 or l2:
            val = carry  # Start with the carry value
            if l1:  # Add value from l1 if it exists
                val += l1.val
                l1 = l1.next
            if l2:  # Add value from l2 if it exists
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)  # Update carry and get the current digit
            current.next = ListNode(val)  # Create a new node with the digit
            current = current.next

        # If there's a remaining carry, add it as a new node
        if carry == 1:
            current.next = ListNode(1)

        return dummy.next
