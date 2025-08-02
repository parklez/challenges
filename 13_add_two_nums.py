# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        This is not the most efficient solution.
        """
        nums = ['', '']

        for index, node in enumerate([l1, l2]):
            current_node = node
            while current_node:
                nums[index] += str(current_node.val)
                current_node = current_node.next

        sum_of_nums = 0
        for num in nums:
            sum_of_nums += int(num[::-1])

        string_sum_of_nums = str(sum_of_nums)[::-1]

        nodes = [ListNode(int(val)) for val in string_sum_of_nums]
        for index, node in enumerate(nodes):
            nodes[index].next = nodes[index+1] if len(nodes) > index + 1 else None

        return nodes[0]
    
    def addTwoNumbersProper(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Explanation:

        1. Dummy Node:
        - We use a dummy node to simplify the linked list construction. It serves as the head of the result list, and we return dummy.next as the final result.
        - current points to the last node in the result list, where we append new nodes.

        2. Iterate with Carry:
        - The loop continues as long as there are digits in l1, l2, or a remaining carry.
        - For each iteration:
            - Extract digits x and y from l1 and l2 (use 0 if the list is exhausted).
            - Compute total = x + y + carry.
            - The new digit is total % 10, and the new carry is total // 10.
            - Create a new node with the digit and append it to the result.
            - Move to the next nodes in l1 and l2 if they exist.

        3. Edge Cases Handled:
        - Lists of different lengths: When one list is exhausted, we use 0 for its digits.
        - Carry at the end: The loop continues if carry is non-zero, ensuring a final node is added if needed (e.g., [9,9,9,9] + [9,9,9,9] → [8,9,9,9,1]).
        - Single-digit lists or zeros: Handled naturally by the loop and default values.
        """

        # Initialize a dummy node to simplify linked list construction
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Continue while there are digits in either list or a carry remains
        while l1 or l2 or carry:
            # Get values from the lists, use 0 if list is exhausted
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the calculated digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print([node.val for node in solution.addTwoNumbers(l1, l2)])
