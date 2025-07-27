# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq
from typing import List


class Solution:

    def topKFrequent_topK(self, nums: List[int], k: int) -> List[int]:
        """My idea behind this solution was something
        along the lines of an Arcade top score!

        For every "score"/iteration of the frequency map,
        check against the top_k "highscores".
        If a new highscore is found, add it to the top_k.
        """

        top_k = {}
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        for num in freq_map:
            # Fill in the top k
            if len(top_k) < k:
                top_k[num] = freq_map[num]
            else:
                # The major downside of my solution is that it has to
                # sort the top_k by its values in ascending order
                top_k = dict(sorted(top_k.items(), key=lambda item: item[1]))
                # Iterate over the top_k
                for top_k_num in top_k:
                    # If the current number has a higher frequency than the lowest
                    # frequency in the top_k, remove it from the top_k
                    if freq_map[num] > top_k[top_k_num]:
                        # Remove the lowest frequency from the top_k
                        del top_k[top_k_num]
                        # Add the current number to the top_k
                        top_k[num] = freq_map[num]
                        # Break out of the loop since we've already found a spot
                        break

        return list(top_k.keys())

    def topKFrequent_Bucket(self, nums: List[int], k: int) -> List[int]:
        # https://www.youtube.com/watch?v=YPTqKIgVk-k
        # O (n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        # Read the array in reverse order
        for i in range(len(freq) - 1, 0, -1):
            # For each value in the bucket
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequent_Heap(self, nums: List[int], k: int) -> List[int]:
        # https://docs.python.org/3/library/heapq.html
        # O(nlogk)
        count = {}
        freq = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            # The idea behind the heap is that it keeps the k highest values (they're the priority queue)
            # As for the tuple logic, it uses the first value for comparisons.
            heapq.heappush(freq, (c, n))
            # If the length of the heap is greater than k, remove the lowest value
            if len(freq) > k:
                heapq.heappop(freq)

        # The last if block is safer than doing freq[:k] down here.
        return [n for c, n in freq]

if __name__ == '__main__':
    solution = Solution()

    nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
    k = 7

    print(solution.topKFrequent_topK(nums, k))
    print(solution.topKFrequent_Bucket(nums, k))
    print(solution.topKFrequent_Heap(nums, k))

