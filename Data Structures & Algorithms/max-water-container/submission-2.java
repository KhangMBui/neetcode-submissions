class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;
        int l = 0;
        int r = heights.length - 1;
        while (l < r) {
            maxArea = Math.max(maxArea, (r - l) * Math.min(heights[r], heights[l]));
            if (heights[l] < heights[r]) {
                l += 1;
            } else if (heights[l] >= heights[r]) {
                r -= 1;
            }
        }
        return maxArea;
    }
}
