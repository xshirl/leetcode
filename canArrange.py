# Two Pointer Approach, All we care about is the numbers modulo k. So convert to a new array modulo K. Sort the array. Then move past all leading zeros, if the index is at an odd index that means there were an odd number of 0's so we cannot make the pairing return False. Otherwise use two pointer from front and back and pair the elements greedily if we run into a pair that is not equal to k return False.


def canArrange(arr, k):
    A = [a % k for a in arr]
    A.sort()
    l = 0
    r = len(A) - 1
    while l < len(A) and A[l] == 0:
        l += 1
    if l % 2 == 1:
        return False
    while l < r:
        if A[l] + A[r] != k:
            return False
        l += 1
        r -= 1
    return True

# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/submissions/
