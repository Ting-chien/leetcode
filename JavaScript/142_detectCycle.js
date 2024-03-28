function ListNode(val) {
    this.val = val;
    this.next = null;
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
  if (!head) return null;
  let pointer = head;
  while (pointer.next !== null) {
    let current = pointer.next;
    pointer.next = null;
    if (findNode(head, current)) {
      pointer.next = current;
      return current;
    }
    pointer.next = current;
    pointer = pointer.next;
  }
  return null;
};

function findNode(head, node) {
  while (head !== null) {
    if (head === node) {
      return node;
    }
    head = head.next;
  }
  return null;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
  let pivot = findPivot(head);
  if (!pivot) return null;
  while (head !== pivot) {
    head = head.next;
    pivot = pivot.next;
  }
  return head;
};

function findPivot(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      return fast;
    }
  }
  return null;
}



let node1 = new ListNode(3);
let node2 = new ListNode(2);
let node3 = new ListNode(0);
let node4 = new ListNode(4);
// let node5 = new ListNode(10);
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node2;
console.log(node1)
console.log(detectCycle(node1));

// let node1 = new ListNode(1);
// let node2 = new ListNode(2);
// node1.next = node2;
// node2.next = node1;
// console.log(detectCycle(node1));

// let node1 = new ListNode(1);
// console.log(detectCycle(node1));