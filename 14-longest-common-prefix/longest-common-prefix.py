class Solution:
    def _longPrefixExtractor(self, strs, idx=0):
        if idx >= len(strs[0]):
            return strs[0][:idx]

        ch = strs[0][idx]

        for word in strs:
            if idx >= len(word) or word[idx] != ch:
                return strs[0][:idx]

        return self._longPrefixExtractor(strs, idx + 1)

    def longestCommonPrefix(self, strs):
        return self._longPrefixExtractor(strs)