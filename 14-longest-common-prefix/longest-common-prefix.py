class Solution:
    def _longPrefixExtractor(self, strs: List[str], output: str="") -> str:
        if not strs[0]:
            return output

        pc = strs[0][0]
        conc = True
        for word in strs:
            if not word:
                conc = False
                break
            elif word[0] == pc:
                continue
            else:
                conc = False
                break
        if not conc:
            return output
        else:
            output += pc
            strs = list(map(lambda x: x[1:], strs))

            return self._longPrefixExtractor(strs, output)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self._longPrefixExtractor(strs)
