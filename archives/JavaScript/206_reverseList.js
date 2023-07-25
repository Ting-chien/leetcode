// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  if (!head) return head;
  let prev = null;
  let current = head;
  let next = current.next;
  while (next !== null) {
    current.next = prev;
    prev = current;
    current = next;
    next = next.next;
  }
  current.next = prev;
  return current;
};

/**
 * @param {ListNode} head
 * @return {ListNode}
 * 
 * 優化：用三數交換的概念去看，[a, b, c] = [b, c, a]
 */
var reverseList = function(head) {
  if (!head || !head.next) return head;
  let prev = null, next = null;
  while (head) {
    // next = head.next;
    // head.next = prev;
    // prev = head;
    // head = next;
    [head.next, prev, head] = [prev, head, head.next]
  }
  return prev;
};

/**
 * @param {ListNode} head
 * @return {ListNode}
 * 
 * Recusion
 */
var reverseList = function(head) {
  if( !head || !head.next) return head;
  var p = head;
  head = reverseList(p.next);
  p.next.next = p;
  p.next = null;
  return head;
};

/**
 * @param {ListNode} head
 * @return {ListNode}
 * 
 * Stack FILO 暴力解
 */
var reverseList = function(head) {
  if( !head || !head.next) return head;
  var p = head;
  head = reverseList(p.next);
  p.next.next = p;
  p.next = null;
  return head;
};

// stack
var reverseList = function(head) {
  if(head === null) return head;
  let stack = [];
  while(head !== null){
      stack.push(head);
      head = head.next;
  }
  let current = stack.pop();
  head = current;
  while(stack.length > 0){
      current.next = stack.pop();
      current = current.next;
  }
  current.next = null;
  return head;
};