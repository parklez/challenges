# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the last seen position of each character
        char_position = {}
        # Initialize the start of the current substring window
        window_start = 0
        # Initialize the maximum length found so far
        max_length = 0

        # Loop through each character in the string using index
        for current_pos, char in enumerate(s):
            # In case a repetition is found, move the "window_start" to
            # +1 the position of the last seen position of said character.
            if char in char_position and char_position[char] >= window_start:
                window_start = char_position[char] + 1
            else:
                # Update max_length if current window is larger
                max_length = max(max_length, current_pos - window_start + 1)

            # Update the last seen position of the current character
            char_position[char] = current_pos

        # Return the length of the longest substring found
        return max_length

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring(" "))
    print(solution.lengthOfLongestSubstring("dvdf"))
