class Solution:
    def addDigits(self, a: str, b: str) -> tuple[str, str | None]:
        if a == b:
            if a == '1':
                return '0', '1'
            else:
                return '0', None
        else:
            return '1', None

    def addBinary(self, a: str, b: str) -> str:
        ai = len(a)
        bi = len(b)
        i = ai if ai > bi else bi
        sum: str = ''
        carry: str | None = None
        while True:
            if i == 0:
                if carry:
                    sum = carry + sum
                break
            else:
                i -= 1
                ai -= 1
                bi -= 1
            x = a[ai] if ai >= 0 else carry
            y = b[bi] if bi >= 0 else carry
            if not x:
                sum = y + sum
                continue
            elif not y:
                sum = x + sum
                continue
            s, c1 = self.addDigits(x, y)
            c2: str | None = None
            if carry and ai >=0 and bi >= 0:
                s, c2 = self.addDigits(s, carry)
            
            carry = '1' if c1 == '1' or c2 == '1' else None

            sum = s + sum

            print(x, y, s, carry, sum)
        
        return sum