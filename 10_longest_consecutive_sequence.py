# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        start_of_streaks = set()
        longest_sequence = 0

        for number in numbers:
            if number - 1 not in numbers:
                start_of_streaks.add(number)

        for start in start_of_streaks:
            current_streak = 1

            i = 1
            while True:
                if start + i in numbers:
                    current_streak += 1
                    i += 1
                    continue
                break

            if current_streak > longest_sequence:
                longest_sequence = current_streak

        return longest_sequence


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutive([]))
    print(solution.longestConsecutive([0, 0, 0]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(solution.longestConsecutive([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]))
    print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
