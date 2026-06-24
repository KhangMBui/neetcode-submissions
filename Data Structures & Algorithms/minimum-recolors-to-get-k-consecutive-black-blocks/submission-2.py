class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # We can recolor a white block so it becomes a black block
        # Return minimum number of operations (coloring) needed such that 
        # there is at least one occurrence of k conseutive black blocks

        # "WBBWWBBWBW" k = 7 => Need 7 black in a row

        # The middle W W and W
        # So basically we count (white_n), keep a minimum of that
        # So our sliding window would have a size of maximum k

        # Run through the blocks with window size = k
        # Each time we do: res = min(res, number of white blocks)

        if not blocks:
            return -1
        
        white_block_count = 0 # To save memory
        res = float("inf")
        l = 0

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                white_block_count += 1

            while r - l + 1 > k:
                if blocks[l] == 'W':
                    white_block_count -= 1
                l += 1
            
            if r - l + 1 == k: # Only evaluate when we have k blocks. Not <= k
                res = min(res, white_block_count)
        
        return res