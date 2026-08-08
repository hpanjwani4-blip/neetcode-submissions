class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        result = []
        for n in range(len(nums)):
            if nums[n] not in res:
                res[nums[n]] = n
            t = target - nums[n]
            if t in res:
                if res[t]!=n:
                    # if abs(nums[n])<abs(t):
                    #     return [n, res[t]]
                    # else:
                    return [res[t], n]