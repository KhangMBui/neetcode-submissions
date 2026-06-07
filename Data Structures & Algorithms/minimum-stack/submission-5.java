class MinStack {
    Stack<Integer> numberStack;
    Stack<Integer> minStack;
    public MinStack() {
        numberStack = new Stack<Integer>();
        minStack = new Stack<Integer>();
    }
    
    public void push(int val) {
        numberStack.push(val);
        val = Math.min(val, minStack.isEmpty() ? val : minStack.peek());
        minStack.push(val);
    }
    
    public void pop() {
        numberStack.pop();
        minStack.pop();
    }
    
    public int top() {
        return numberStack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
