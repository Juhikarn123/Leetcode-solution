class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j=0
        n=len(nums)
        while j<n:
            s=(j+n)//2
            if nums[s]==target:
                return s
            if nums[s]<target:
                j=s+1
            else:
                n=s
        return j
