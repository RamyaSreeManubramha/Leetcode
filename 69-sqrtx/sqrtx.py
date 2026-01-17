class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        y=0
        end=x
        l=1
        while l<=end:
            mid=(l+end)//2
            if mid*mid<=x:
                y=mid
                l=mid+1
            else:
                end=mid-1
        return y
