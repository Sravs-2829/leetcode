class Solution:
    def digitFrequencyScore(self, n: int) -> int:
     
        freq = {}

        for digit in str(n):
            freq[digit] = freq.get(digit, 0) + 1

        ans = 0
        for digit, count in freq.items():
            ans += int(digit) * count

        return ans        