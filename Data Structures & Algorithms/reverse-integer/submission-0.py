class Solution:
    def reverse(self, x: int) -> int:

        limit = 2**32 -1
        postive = True
        if x < 0:
            postive = False
            x = abs(x)
        rev = 0
        while x:
            rem = x%10
            rev = rev * 10 + rem
            x = x // 10
        if rev > limit:
            return 0
        return rev if postive else rev*-1
        