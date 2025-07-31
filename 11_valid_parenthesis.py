# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Important points:
        - The stack is LIFO
        - Stacks can't start with closing parenthesis
        - The top of the stack must be the corresponding opening parenthesis
        """

        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for char in s:
            
            if char in parenthesis.values():
                stack.append(char)

            elif stack and char in parenthesis.keys() and stack[-1] == parenthesis[char]:
                stack.pop()

            else:
                return False

        return not stack

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()'))
    print(solution.isValid('()(()())'))
    print(solution.isValid('((()))'))
    print(solution.isValid('(()'))
    print(solution.isValid(')()('))

