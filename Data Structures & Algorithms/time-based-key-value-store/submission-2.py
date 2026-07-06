class TimeMap:
    def __init__(self):
        self.dictionary = {}  # ( (key, timestamp): value) ; O(n) space

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_tuple = (key, timestamp)
        self.dictionary[key_tuple] = value # O(1) time

    def get(self, key: str, timestamp: int) -> str:
        for time in range(timestamp, -1, -1): # O(n) time, where n is timestamp
            key_tuple = (key, time)
            print("current key tuple: ", key_tuple)
            if key_tuple in self.dictionary:
                return self.dictionary.get(key_tuple)
        return ""