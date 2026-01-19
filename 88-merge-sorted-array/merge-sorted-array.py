class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n!=0:
            for i in range(n):
                index=nums1.index(0)
                nums1[index]=nums2[i]
            nums1.sort()

        