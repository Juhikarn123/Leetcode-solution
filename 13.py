class Solution:
    def romanToInt(self, s: str) -> int:
        sol=0
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for x,y in zip(s,s[1:]):
            if roman[x]<roman[y]:
                sol-=roman[x]
            else:
                sol+=roman[x]
        return sol+roman[s[-1]]
