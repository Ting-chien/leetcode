class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.length = 0;
    this.head = null;
  }
  // Push node to the tail
  append(item) {
    let node = new Node(item);
    if (!this.head) {
      this.head = node;
    } else {
      let current = this.head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = node;
    }
    this.length ++;
  }
  // Delete node at index
  removeAt(index) {
    if (index < 0 || index > this.length) return null;
    let current = this.head, prev = null, currentIndex = 0;
    if (index === 0) {
      this.head = current.next;
    } else {
      while (currentIndex++ < index) {
        prev = current;
        current = current.next;
      }
      prev.next = current.next;
    }
    this.length --;
  }
  // Delete node from value
  removeFrom(item) {
    let current = this.head, prev = null;
    while (current.next !== null || current.item !== item) {
      prev = current;
      current = current.next;
    }
    if (current === this.head) {
      this.head = current.next;
    } else {
      prev.next = current.next;
    }
    this.length --;
  }
}

let list = new LinkedList();
list.append(1);
list.append(3);
list.append(10);
list.removeAt(1);
list.removeFrom(10);

console.log(list);