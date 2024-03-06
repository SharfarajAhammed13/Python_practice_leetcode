# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Thank you neetcode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False 
    
# Explanation
# This code is an implementation of Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm. It is used to detect whether a linked list contains a cycle or not.

# Here's a step-by-step explanation:

# 1. The function `hasCycle` takes the head of a linked list as input.

# 2. Two pointers, `slow` and `fast`, are initialized to the head of the linked list.

# 3. In the `while` loop, the `fast` pointer moves two steps at a time, and the `slow` pointer moves one step at a time. This is the key idea behind the algorithm.

# 4. The loop continues as long as both `fast` and `fast.next` are not `None`. If there is a cycle in the linked list, the `fast` pointer will eventually catch up to the `slow` pointer.

# 5. Inside the loop, after the pointer movements, there is a check to see if `slow` and `fast` have met (`slow == fast`). If they meet, it indicates the presence of a cycle, and the function returns `True`.

# 6. If the loop completes without the pointers meeting, it means there is no cycle in the linked list, and the function returns `False`.

# The algorithm takes advantage of the fact that if there is a cycle, the fast pointer will eventually catch up to the slow pointer, creating a loop. If there is no cycle, the fast pointer will reach the end of the linked list (`fast` or `fast.next` will become `None`) before the slow pointer, and the loop will terminate without detecting a cycle.