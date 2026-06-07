class Solution {
    public List<String> generateParenthesis(int n) {
        // Only add string when open == close == n
        // Only add open when open < n
        // Only add close when close < open
        Stack<String> stack = new Stack<String>();
        List<String> res = new ArrayList<>();
        backtrack(n, 0, 0, stack, res);
        return res;
    }
    private void backtrack(int n, int openN, int closeN, Stack<String> stack, List<String> res) {
            if (openN == closeN && openN == n) {
                StringBuilder sb = new StringBuilder();
                for (String c : stack) {
                    sb.append(c);
                }
                res.add(sb.toString());
                return;
            }
            if (openN < n) {
                stack.push("(");
                backtrack(n, openN + 1, closeN, stack, res);
                stack.pop();
            }
            if (closeN < openN) {
                stack.push(")");
                backtrack(n, openN, closeN + 1, stack, res);
                stack.pop();
            }
     };
}
