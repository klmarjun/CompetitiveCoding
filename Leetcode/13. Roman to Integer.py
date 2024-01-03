class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_dictionary = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev_val = 0
        res =0
        for i in reversed(s):
            curr_val = roman_int_dictionary[i]
            if(curr_val>=prev_val):
                res+=curr_val
            else:
                res -= curr_val
            prev_val = curr_val
        return res