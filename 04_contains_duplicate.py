# https://leetcode.com/problems/contains-duplicate/description/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicateSet(self, nums: List[int]) -> bool:
        checked = set()
        # This way we could return the first duplicate at given order
        for number in nums:
            if number in checked:
                return True
            checked.add(number)
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 1]))
    print(solution.containsDuplicate([1, 2, 3, 4]))
    print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
