class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res , part = [], []

        def helper(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.checkPali(s, i, j):
                    part.append(s[i: j+1])
                    helper(j+1)
                    part.pop()
        helper(0)
        return res

    def checkPali(self, s: str, l:int, r:int)-> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

        