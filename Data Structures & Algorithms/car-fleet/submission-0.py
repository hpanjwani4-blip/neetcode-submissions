class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        res = 1
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        times = []
        for car in cars:
            times.append(float((target - car[0])/car[1]))
        max = 0
        for i in range(1, len(times)):
            if times[i-1] > max:
                max = times[i-1]
            if times[i] > max:
                res +=1
            
        return res

            