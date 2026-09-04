import math
class Solution:
    def calc_time(self, rate, piles):
        time = 0
        for pile in piles:
            if pile <= rate:
                time += 1
            else:
                time += math.ceil(pile/rate)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)

        while l<=r:
            rate = (l+r)//2
            time = self.calc_time(rate, piles)
            if time > h:
                l = rate + 1
            else:
                r = rate - 1
        return l