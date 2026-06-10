class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):  # for each bit position
            bit_sum = 0
            for num in nums:
                
                bit_sum += (num >> i) & 1

            
            bit_sum %= 3

            
            if i == 31 and bit_sum:
                result -= (1 << i)
            else:
                result |= (bit_sum << i)

        return result
