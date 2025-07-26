# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Check if the length of both strings are equal
        if len(s) != len(t):
            return False

        counter = {}
        # 2. Count the occurences of each char in S
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        # 3. For each char in T check if it exists in S and if the number of occurences is equal
        for char in t:
            # Example: Let's say 'A' shows up 2 times in A.
            # For each loop here, if a 3rd occurence of 'A' is found in T,
            # the counter will be 0 and the function will return False
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
    
    def isAnagramCounter(self, s: str, t: str) -> bool:
        # Making "Counter" objects from both strings and comparing is enough.
        # Comparing list lengths is not even needed!
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('ABA', 'AAA'))