class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(index, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            for c in digitToChar[digits[index]]:
                helper(index+1, curr_str+c)

            
        if digits:
            helper(0, "")
        
        return res
        