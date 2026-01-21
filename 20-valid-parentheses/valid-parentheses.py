class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(0,len(s)):
            if s[i]=='(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i]==')' or s[i] == ']' or s[i] == '}':
                if not stack:
                    return False
                last_ele=stack.pop()
                if s[i]==')' and last_ele!='(':
                    return False
                if s[i]==']' and last_ele!='[':
                    return False
                if s[i]=='}' and last_ele!='{':
                    return False
        if not stack:
            return True
        else:
            return False
                