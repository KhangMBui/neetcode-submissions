class MinStack {
    constructor() {
        this.minStack = [];
        this.numStack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.numStack.push(val);
        val = Math.min(val, this.minStack.length === 0 ? val : this.minStack[this.minStack.length - 1]);
        this.minStack.push(val);
    }

    /**
     * @return {void}
     */
    pop() {
        this.minStack.pop();
        this.numStack.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.numStack[this.numStack.length - 1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack[this.minStack.length - 1];
    }
}
