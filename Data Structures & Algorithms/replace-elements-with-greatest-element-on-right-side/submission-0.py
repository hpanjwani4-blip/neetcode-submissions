class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
            
        def find_max_value(arr: List[int], start):
            max = -1
            index = 0
            res = ()
            for i in range(start,len(arr)):
                if arr[i]>max:
                    max = arr[i]
                    index = i
            res = (max,index)
            return(res)
        res = find_max_value(arr,0)
        for i in range (len(arr)):
            print(res[1])
            print(i)
            if res[1]>i:
                arr[i] = res[0]
            else:
                res = find_max_value(arr,i+1)
                arr[i] = res[0]
        return arr