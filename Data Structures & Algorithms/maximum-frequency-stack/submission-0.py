class FreqStack:

    def __init__(self):
        # Tracks frequency of each value
        self.freq = defaultdict(int)

        # Tracks groups of certain frequencies
        self.group = defaultdict(list) # frequency as key, list is the value that has that frequencies

        # Tracks the current highest frequency
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1

        # This stack reserves recency, as the more on-top values are at the back
        self.group[self.freq[val]].append(val)

        self.max_freq = max(self.max_freq, self.freq[val])
        
    def pop(self) -> int:
        val = self.group[self.max_freq].pop()

        self.freq[val] -= 1

        # If no values remain at this max frequency, decreases frequency
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()