class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0]*n
        for i in range(n):
            if stack:
                while stack and temperatures[stack[-1]] <= temperatures[n-1-i] :
                    stack.pop()
                if stack:
                    result[n-1-i] = stack[-1] - (n-i-1)
            stack.append(n-1-i)
        return result

