# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        This is the O(n) solution.
        https://www.youtube.com/watch?v=bNvIQI2wAjk
        """
        result = [1] * len(nums)

        # Calculate the prefix products
        prefix = 1
        for i in range(len(nums)):
            result[i] = result[i] * prefix
            prefix = prefix * nums[i]

        # Calculate the postfix products
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result

    def productExceptSelfDivision(self, nums: List[int]) -> List[int]:
        """
        This does not work when there's a 0 in the array!
        Also the problem does not allow you to use division...
        """
        result = 1
        array = []
        for num in nums:
            result = result * num

        for num in nums:
            array.append(result // num if num else 0)

        return array

    def productExceptSelfON2(self, nums: List[int]) -> List[int]:
        """
        This is the O(n^2) solution, which is too slow...
        """
        array = [1] * len(nums)

        for index, num in enumerate(nums):
            for num_index, _ in enumerate(array):
                if num_index != index:
                    array[num_index] = array[num_index] * num

        return array


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
