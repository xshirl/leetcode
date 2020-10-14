# https://leetcode.com/problems/single-number-iii/discuss/750633/Python-O(1)-space-and-O(n)-time-Turn-into-easy-Single-Number-problem


class Solution:
    def singleNumber(self, nums):

        # Take XOR of entire array. This will cancel out all pairs
        nums_xor = 0
        for num in nums:
            nums_xor ^= num

        # nums_xor is now the XOR of sought 'a' and 'b'
        # We now loop over every bit in nums_xor to find the first set bit
        # The first set bit will be the first occurence where 'a' and 'b' differ (looking at the bits).

        x = 1
        bit_pos = 0

        # Loop over all bits in 32 bit integer to find first instance where the bits of 'a' and 'b' differ
        for i in range(31):
            # Check if bit is set. If true then break out of loop
            if nums_xor & x:
                bit_pos = i
                break
            # Move bit for x to check next bit
            x <<= 1

        # Now we have found the first bit the differ between 'a' and 'b'
        # That means that if we loop over nums again, looking only at numbers with bit set, at bit_pos then:
        # If we say that the bit is set for the number 'a', 'a' will have the bit set and also some pairs
        # in nums have the bit set (but not 'b'!)
        # This means that if we take XOR of all numbers with the bit set this will cancel the pairs
        # leaving us only with 'a'
        # Reversly, if we take XOR of all numbers with bit not set, this will cancel all remaining pairs
        # leaving us only with 'b'

        x = 1 << bit_pos
        a = 0
        b = 0

        # Loop over nums again
        for num in nums:
            if num & x:
                a ^= num
            else:
                b ^= num

        return [a, b]
