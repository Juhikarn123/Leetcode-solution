class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for j,n in reversed(list(enumerate(digits))):
            if n<9:
                digits[j]+=1
                return digits
            digits[j]=0
        return[1]+digits
