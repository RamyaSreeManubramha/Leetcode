class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                i+=1
                j+=1
            else:
                i+=1
    