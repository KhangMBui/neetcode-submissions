class TimeMap:
    def __init__(self):
        self.dictionary = defaultdict(list)  # {key : [(timestamp, value), etc.]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value)) # O(1)

    def get(self, key: str, timestamp: int) -> str:
        if not self.dictionary[key]:
            return ""

        arr = self.dictionary[key]

        l, r = 0, len(arr) - 1
        res = ""
        
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]
            elif arr[m][0] < timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res