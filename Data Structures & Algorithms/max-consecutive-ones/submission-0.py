class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max = max+1
                if max>res:
                    res = max
            else:
                max = 0

        return res


        
        