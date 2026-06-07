class MinStack {
    Stack<Integer> numStack;
    Stack<Integer> minStack;
    public MinStack() {
        numStack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        numStack.push(val);
        val = Math.min(val, minStack.isEmpty() ? val : minStack.peek());
        minStack.push(val);
    }
    
    public void pop() {
        numStack.pop();
        minStack.pop();
    }
    
    public int top() {
        return numStack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
