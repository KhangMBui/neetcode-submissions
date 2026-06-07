class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a hashmap to store {number:frequency}
        # Then convert {number:frequency} into [[list of numbers]], with each list's position
        # at the index of the frequency
        # sort it based on frequency, then retrieve list of numbers and add to res

        if not nums:
            return []

        num_count = Counter(nums)
        
        max_freq = max(num_count.values())

        freq_to_number = [[] for _ in range(max_freq + 1)]

        for num, count in num_count.items():
            freq_to_number[count].append(num)
        
        # Now iterate the array backward until we have k elements
        res = []
        for arr in freq_to_number[::-1]:
            for n in arr:
                res.append(n)
                if len(res) == k:
                    return res
        return res


