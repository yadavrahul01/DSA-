class Solution:
    def singleNumber(self,nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    ## Time complexicity = O(n)
    ## Space complexicity = O(1)