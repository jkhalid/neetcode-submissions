class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        curr_combo = []
        candidates.sort()

        def helper(i, total):
            if total == target:
                result.append(curr_combo.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            curr_combo.append(candidates[i])
            helper(i+1, candidates[i]+ total)
            curr_combo.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            helper(i+1, total)

        helper(0, 0)
        return result
        