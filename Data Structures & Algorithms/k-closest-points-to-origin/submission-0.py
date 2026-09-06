import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        output = []
        for point in points:
            dist = math.sqrt((point[0]**2) + (point[1]**2))
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)
        
        for i in pq:
            output.append(i[1])
        return output


        