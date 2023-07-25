/**
 * Initialize your data structure here.
 */
var MyStack = function() {
  this.inQueue = [];
  this.outQueue = [];
};

/**
 * Push element x onto stack. 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
  this.inQueue.push(x);
};

/**
 * Removes the element on top of the stack and returns that element.
 * @return {number}
 */
MyStack.prototype.pop = function() {
  while (this.inQueue.length > 1) {
    this.outQueue.push(this.inQueue.shift());
  }
  const lastItem = this.inQueue.shift();
  [this.inQueue, this.outQueue] = [this.outQueue, this.inQueue];
  return lastItem;
};

/**
 * Get the top element.
 * @return {number}
 */
MyStack.prototype.top = function() {
  while (this.inQueue.length > 1) {
    this.outQueue.push(this.inQueue.shift());
  }
  const lastItem = this.inQueue[0];
  this.outQueue.push(this.inQueue.shift());
  [this.inQueue, this.outQueue] = [this.outQueue, this.inQueue];
  return lastItem;
};

/**
 * Returns whether the stack is empty.
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
  return this.inQueue.length === 0;
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */