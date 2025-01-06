class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        rows = [""]*numRows
        row = 0
        step = 1

        for i in s:
            rows[row]+=i
            row+=step

            if row==0 or row ==numRows-1:
                step*=-1
        return "".join(rows)