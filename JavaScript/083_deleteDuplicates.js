// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
  let current = head;
  while (current !== null && current.next !== null) {
    if (current.val === current.next.val) {
      current.next = current.next.next;
      continue;
    }
    current = current.next;
  }
  return head;
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 * 
 * AC助教解法，基本上概念與我的相同，但寫法更精簡
 */
var deleteDuplicates = function(head) {
  // maybe cause memory leak.
  let curr = head
  while(curr && curr.next) {
    if (curr.val === curr.next.val) {
      curr.next = curr.next.next
    } else {
      curr = curr.next
    }
  }
}

let node1 = new ListNode(1);
let node2 = new ListNode(1);
let node3 = new ListNode(1);
let node4 = new ListNode(3);
let node5 = new ListNode(3);
node1.next = node2;
node2.next = node3;
// node3.next = node4;
// node4.next = node5;
console.log(node1);
console.log(deleteDuplicates(node1))