# https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Create a stack and set the first element to -1
        # The stack will store the indices of the opening parentheses
        stack = [-1]
        
        # Set the maximum length of valid parentheses to 0
        max_len = 0

        # Iterate over the string
        for i in range(len(s)):
            # If the character is an opening parenthesis, push it to the stack
            current_char = s[i]
            if current_char == "(":
                stack.append(i)
            # If the character is a closing parenthesis
            else:
                # Pop the stack (remove the last opening parenthesis)
                stack.pop()
                # If the stack is empty, push the current index
                if len(stack) == 0:
                    stack.append(i)
                # If the stack is not empty, calculate the length of the valid parentheses
                else:
                    # The length is the difference between the current index and the last opening parenthesis
                    # Update the maximum length if the current length is greater
                    max_len = max(max_len, i - stack[-1])

        # Return the maximum length of valid parentheses
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("(()"))
    print(solution.longestValidParentheses(")()())"))
    print(solution.longestValidParentheses(""))
