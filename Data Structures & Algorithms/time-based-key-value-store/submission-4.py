class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp,value))
        else:
            self.store[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        left = 0
        n = len(self.store[key])
        right = n-1
        l = self.store[key]
        while left <= right:
            mid = (left+right)//2
            if l[mid][0] == timestamp:
                return l[mid][1]

            elif l[mid][0]<timestamp:
                left = mid+1
            
            else:
                right = mid-1
        if right<0:
            return ""
            

        else:
            return l[right][1]
            



        
