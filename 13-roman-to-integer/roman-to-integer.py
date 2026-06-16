class Solution:
    # parse block
    # build block
    # add total
    # mapper
    ROMAN_DICT = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def _get_index_of_key(self, key: str) -> int:
        return list(self.ROMAN_DICT.keys()).index(key)

    def _mapper(self, key: str) -> int:
        return self.ROMAN_DICT.get(key, 0)
    
    def _parse_block(self, block: str) -> int:
        value=0
        for i in range(len(block)):
            char=block[i]
            weight = self._mapper(char)
            value=abs(weight-value)
        
        return value
    
    def _build_block(self, roman: str) -> (str, str | None):
        length = len(roman)
        if length == 1:
            return roman, None
        else:
            # if more than 1 length, extract first two chars
            # check if their values are in two step range or first one is more than second
            firstChar = roman[0]
            secChar = roman[1]
            firstIdx = self._get_index_of_key(firstChar) 
            secIdx = self._get_index_of_key(secChar) 
    
            if firstIdx >= secIdx:
                return firstChar, roman[1:]
            else:
                return roman[:2], roman[2:]

    def romanToInt(self, s: str) -> int:
        value = 0
        new_s = s
        while True:
            block, new_s = self._build_block(new_s)

            value += self._parse_block(block)

            if not new_s:
                break

        return value
 

