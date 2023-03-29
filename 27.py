class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for number in nums:
            if number!=val:
                nums[j]=number
                j=j+1
        return j
