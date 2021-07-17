class Node {
  constructor(data) {
    this.data = data;
    this.left = this.right = null;
  }
  // insert
  insert(value) {
    // 如果value<=data，設為left child node，反之為right child node
    if (value <= this.data) {
      // 如果child node為空，則建立新的node，反之繼續往下搜尋
      if (!this.left) {
        this.left = new Node(value);
      } else {
        this.left.insert(value);
      }
    } else {
      if (!this.right) {
        this.right = new Node(value);
      } else {
        this.right.insert(value);
      }
    }
  }
  // find node
  contains(value) {
    if (value === this.data) {
      return true;
    } else if (value < this.data) {
      if (!this.left) {
        return false;
      } else {
        return this.left.contains(value);
      }
    } else {
      if (!this.right) {
        return false;
      } else {
        return this.right.contains(value);
      }
    }
  }
  // in-order print out
  printInOrder() {
    if (this.left) {
      this.left.printInOrder();
    }
    console.log(this.data);
    if(this.right) {
      this.right.printInOrder();
    }
  }
}