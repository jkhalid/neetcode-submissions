# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.merge_sort(pairs, 0, len(pairs))
    
    def merge_sort(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        if end - start + 1 <= 1:
            return pairs
        
        mid = (start + end) // 2
        self.merge_sort(pairs, start, mid)
        self.merge_sort(pairs, mid + 1, end)

        self.merge(pairs, start, mid, end)

        return pairs
    
    def merge(self, pairs: List[Pair], start: int, mid:int ,end: int):
        Left = pairs[start: mid+1]
        Right = pairs[mid+1: end+1]

        l , r, k = 0, 0, start

        while l < len(Left) and r < len(Right):
            if Left[l].key <= Right[r].key:
                pairs[k] = Left[l]
                l +=1
            else:
                pairs[k] = Right[r]
                r+=1
            k+=1

        while l < len(Left):
            pairs[k] = Left[l]
            l+=1
            k+=1
        while r < len(Right):
            pairs[k] = Right[r]
            r+=1
            k+=1


