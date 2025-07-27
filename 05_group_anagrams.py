# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for sub_string in strs:
            # It's crucial to find a unique key for each anagram.
            # Sorting the string will guarantee a unique key.
            # Eg. bca -> abc
            anagram_key = ''.join(sorted(sub_string))
            if anagram_key in anagrams:
                anagrams[anagram_key].append(sub_string)
            else:
                anagrams[anagram_key] = [sub_string]

        return list(anagrams.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
