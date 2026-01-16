class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long_pre=[]
        if strs and len(strs) > 0:
            strs=sorted(strs)
            first,last=strs[0],strs[-1]
            for i in range(len(first)):
                if len(last)>i and first[i]==last[i]:
                    long_pre.append(first[i])
                else:
                    return "".join(long_pre)
        return "".join(long_pre)
        
