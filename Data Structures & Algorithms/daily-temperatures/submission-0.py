class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        stack.append(0)
        for i in range(1,len(temperatures)):
            while stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    result = i - stack[-1]
                    res[stack[-1]] = result
                    stack.pop()
                else:
                    break
            stack.append(i)

        return res
