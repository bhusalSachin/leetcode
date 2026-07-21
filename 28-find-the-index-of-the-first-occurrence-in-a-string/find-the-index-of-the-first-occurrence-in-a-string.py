class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        oc = -1

        for i in range(0, len(haystack)):
            sstring = haystack[i:len(needle)+i]
            # print(i, haystack, needle, sstring)
            if sstring == needle:
                oc = i
                break
        
        return oc