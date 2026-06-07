class MinStack {
private:
    std::stack<int> numStack;
    std::stack<int> minStack;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        numStack.push(val);
        val = std::min(val, minStack.empty() ? val : minStack.top());
        minStack.push(val);
    }
    
    void pop() {
        numStack.pop();
        minStack.pop();
    }
    
    int top() {
        return numStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
