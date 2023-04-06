class Solution:
    def climbStairs(self, n: int) -> int:
        juhi=[1,1]+[0]*(n-1)
        for i in range(2,n+1):
            juhi[i]=juhi[i-1]+juhi[i-2]
        return juhi[n]
