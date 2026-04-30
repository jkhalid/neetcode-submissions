class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False
        hand_map = Counter(hand)

        min_heap = list(hand_map.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            for i in range(start, start + groupSize):
                if i not in hand_map:
                    return False
                hand_map[i] -=1
                if hand_map[i] == 0:
                    if i!= min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True

        