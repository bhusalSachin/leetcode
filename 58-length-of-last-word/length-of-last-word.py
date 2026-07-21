class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned = s.strip()
        return len(cleaned[cleaned.rfind(" ")+1:])