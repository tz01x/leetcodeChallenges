import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for num in range(1, n+1):
            num *= num
            for t in range(num, n + 1):
                dp[t] = min(dp[t], 1 + dp[t - num])

        return dp[n]

            
    
        

s = Solution()

items = [12,13,45,43,4869]
for item in items:
    print(s.numSquares(item))