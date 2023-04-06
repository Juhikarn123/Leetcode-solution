class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=m-1
        s=n-1
        k=m+n-1
        while s>=0:
            if j>=0 and nums1[j]>nums2[s]:
                nums1[k]=nums1[j]
                k-=1
                j-=1
            else:
                nums1[k]=nums2[s]
                k-=1
                s-=1
