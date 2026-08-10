class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict()
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        for num, count in freq.items():
            buckets[count].append(num)

        for bucket in buckets[::-1]:
            if bucket:
                for buck in bucket:
                    res.append(buck)
                    if(len(res)==k):
                        return (res)

        # print(buckets)
        
        