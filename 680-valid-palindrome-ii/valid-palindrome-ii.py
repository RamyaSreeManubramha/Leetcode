class Solution:
    def palindrome(self, s, left, right):
        while left<=right:
            if s[left]==s[right]:
                left=left+1
                right=right-1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]==s[right]:
                left=left+1
                right=right-1
            else:
                return self.palindrome(s,left+1,right) or self.palindrome(s,left,right-1)
        return True