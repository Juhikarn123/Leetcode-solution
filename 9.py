class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        revert=0
        y=x
        while y:
            revert=revert*10+y%10
            y=y//10
        return revert==x
