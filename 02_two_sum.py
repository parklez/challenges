# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)
        for index, num in enumerate(nums):
            next_index = index+1
            for index_pair, pair in enumerate(nums[next_index:]):
                if num + pair == target:
                    return [index, next_index + index_pair]

    def twoSumOnePass(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        hash_table = {}
        for index, num in enumerate(nums):
            # Check if we've already come across an element (complement, eg. target - num)
            # that adds up to the target!
            if target - num in hash_table:
                return [hash_table[target - num], index]
            hash_table[num] = index

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSumOnePass([2, 7, 11, 15], 9))
