import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
        while len(pq) > 1:
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(pq, -(y-x))
            else:
                heapq.heappush(pq, -(x-y))
        if not pq:
            return 0
        return -pq[0]

        