class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        result = [0] * n
        carry = 1
        for i in range(n-1, -1, -1):
            val = digits[i] + carry
            if val < 10:
                carry = 0
                result[i] = val
            else:
                result[i] = 0
        if carry == 1:
            result.insert(0, 1)
        return result

        