class Solution:
    def romanToInt(self, s: str) -> int:
        rv={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        integer=0
        for i in range(0,(len(s)-1)):
            if rv[s[i]] < rv[s[i+1]]:
                integer=integer-rv[s[i]]
            else:
                integer=integer+rv[s[i]]
        integer+=rv[s[-1]]
        return integer 