class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = list(zip(position, speed))
        cars.sort()
        answer = n
        slowesttime = (target - cars[n-1][0])/cars[n-1][1]
        for i in range(n-2,-1,-1):
            if (target - cars[i][0])/cars[i][1] <= slowesttime:
                answer-=1
            else:
                slowesttime = (target - cars[i][0])/cars[i][1]
        return answer