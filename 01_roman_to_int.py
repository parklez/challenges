# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        'III'
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numeral_len = len(s)
        _sum = 0
        for index, char in enumerate(s):
            if index + 1 < numeral_len and symbols[s[index]] < symbols[s[index + 1]]:
                _sum -= symbols[char]
                continue
            _sum += symbols[char]

        return _sum

if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('III'))
    print(solution.romanToInt('IV'))
    print(solution.romanToInt('IX'))
    print(solution.romanToInt('LVIII'))
    print(solution.romanToInt('MCMXCIV'))
