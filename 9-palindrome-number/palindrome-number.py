class Solution:
    def isPalindrome(self, x: int) -> bool: # x = -121
        z = x
        y = 0 
        length = len(str(x))
        for i in range(length): 
            y = y*10 + z % 10 # z = -1, -12, -121

            z = z // 10 # z = -12, -1, 0

        if y == x:
            return True
        else:
            return False
