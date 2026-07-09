class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1

        while l < r:
            check = numbers[l] + numbers[r]
            if check == target:
                return [l+1, r+1]
            elif check > target:
                r-=1
            else:
                l+=1
        return []
        