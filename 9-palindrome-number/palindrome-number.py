class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            y=0
            z=x
            while z!=0:
                reminder=z%10
                remaining=z//10
                y=y*10+reminder
                z=remaining
            if x==y:
                return True
            else:
                return False
