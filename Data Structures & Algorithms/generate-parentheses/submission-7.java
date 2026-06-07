class Solution {
    public List<String> generateParenthesis(int n) {
        // Only add parenthesis when open == close == n
        // Only add ( when open < n
        // Only add ) when close < open
        Stack<Character> stack = new Stack<>();
        List<String> result = new ArrayList<>();
        backtrack(0, 0, n, stack, result);
        return result;
    }
    private void backtrack(int openN, int closeN, int n, Stack<Character> stack, List<String> result) {
        if (openN == closeN && openN == n) {
            StringBuilder sb = new StringBuilder();
            for (char c : stack) {
                sb.append(c);
            }
            result.add(sb.toString());
            return;
        }
        if (openN < n) {
            stack.push('(');
            backtrack(openN + 1, closeN, n, stack, result);
            stack.pop();
        }
        if (closeN < openN) {
            stack.push(')');
            backtrack(openN, closeN + 1, n, stack, result);
            stack.pop();
        }
    }
}
