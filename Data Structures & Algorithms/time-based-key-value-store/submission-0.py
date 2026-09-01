class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l = 0
        r = len(self.store[key]) - 1
        prev_idx = -1

        while l<=r:
            mid = (l+r)//2

            if self.store[key][mid][1] == timestamp:
                return self.store[key][mid][0]
            elif self.store[key][mid][1] < timestamp:
                prev_idx = max(mid, prev_idx)
                l = mid + 1
            else:
                r = mid - 1
        if prev_idx == -1:
            return ""
        return self.store[key][prev_idx][0]
        
