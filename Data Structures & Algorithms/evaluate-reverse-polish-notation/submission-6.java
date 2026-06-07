class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> numberStack = new Stack<Integer>();
        for (int i = 0; i<tokens.length; i++) {
            if (tokens[i].equals("+")) {
                numberStack.push(numberStack.pop() + numberStack.pop());
            }
            else if (tokens[i].equals("-")) {
                int a =  numberStack.pop(); 
                int b = numberStack.pop();
                numberStack.push(b - a);
            }
            else if (tokens[i].equals("*")) {
                numberStack.push(numberStack.pop() * numberStack.pop());
            }
            else if (tokens[i].equals("/")) {
                int a = numberStack.pop();
                int b = numberStack.pop();
                numberStack.push( (int) ((float)(b/a)));
            }
            else {
                numberStack.push(Integer.parseInt(tokens[i]));
            }
        }
        return numberStack.peek();
    }
}
