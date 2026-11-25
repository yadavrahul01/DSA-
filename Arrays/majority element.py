## we have to find the majority element by considering the fact that the majority element
## is the element that appears more than n/2 times in the array.
class Solution:
    def majorityElemenmt(self,nums):
        candidate=None
        count=0
        for num in nums:
            if count == 0:
                candidate=num
            count += (1 if num==candidate else -1)
        return candidate

    ## Time complexicity = O(n)
    ## Space complexicity = O(1)