class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        res = {}
        result = 1
        if not nums:
            return 0
        for num in nums:
            hm[num] = 1

        for num in hm.keys():
            
            res[num] = 1
            i = num
            if hm[num] == 0:
                continue
            while i+1 in hm:
                if i+1 in res:
                    res[num] = res[num]+res[i+1]
                    if res[num]>result:
                        result = res[num]
                    break
                hm[i+1] = 0;
                res[num] = res[num]+1
                if res[num]>result:
                    result = res[num]
                i = i+1
        return result
