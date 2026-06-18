class Solution:
    PARENTHESES_DICT = {
        "(": ")",
        "[":"]",
        "{":"}"
    }

    def is_open(self, bracket: str) -> bool:
        closed_bracket = self.PARENTHESES_DICT.get(bracket, None)
        if closed_bracket:
            return True
        else:
            return False
    
    def check_validity(self, s: str, stack: str = "") -> bool:
        if not s and not stack:
            return True
        elif not s and stack:
            return False

        char = s[0]

        if not self.is_open(char) and not stack:
            return False
        elif not self.is_open(char) and stack:
            prev_opened = stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            prev_close_bracket = self.PARENTHESES_DICT.get(prev_opened)
            if char == prev_close_bracket:
                return self.check_validity(s[1:], stack)
            else: 
                return False
        else:
            stack += char
            return self.check_validity(s[1:], stack)

    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        else:
            return self.check_validity(s)