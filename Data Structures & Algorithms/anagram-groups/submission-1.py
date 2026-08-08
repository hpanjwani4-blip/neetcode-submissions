from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            # print(sorted_s)
            groups[sorted_s].append(s)

        return list(groups.values())