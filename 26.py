class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for n in nums:
            if j<1 or n>nums[j-1]:
                nums[j]=n
                j=j+1
        return j
