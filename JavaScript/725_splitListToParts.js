// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */
// var splitListToParts = function(head, k) {
//   // linked-list is null
//   if (!head) return Array(k).fill(null);
//   const result = [];
//   let counts = counting(head);
//   let quotient = Math.floor(counts / k);
//   let remainder = counts % k;
//   for (let i=0; i<k; i++) {
//     let newHead = null;
//     let current = null;
//     let quotientCounts = quotient;
//     while (quotientCounts > 0) {
//       if (quotientCounts === quotient) {
//         newHead = new ListNode(head.val);
//         current = newHead;
//       } else {
//         current.next = new ListNode(head.val);
//         current = current.next;
//       }
//       head = head.next;
//       quotientCounts --;
//     }
//     if (remainder > 0) {
//       if (newHead === null) {
//         newHead = new ListNode(head.val);
//       } else {
//         current.next = new ListNode(head.val);
//         current = current.next;
//       }
//       head = head.next;
//       remainder --;
//     }
//     result.push(newHead);
//   }
//   return result;
// };

// function counting(head) {
//   let count = 0;
//   while (head !== null) {
//     count ++;
//     head = head.next;
//   }
//   return count;
// }

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
  let listLength = 0
  let tmp = head // [1,2,3,4,5,6,7,8,9,10]
  let ret = []
  
  for(let i = 0; i < k; i++) {
    ret.push(null)
  } // [null, null, null]
  
  while(tmp) {
    listLength = listLength + 1
    tmp = tmp.next
  }
  
  let partLength = Math.floor(listLength / k)
  if (partLength <= 0) partLength = 1
  let extraLength = 0
  if (listLength > k) {
    extraLength = listLength % k // 10 除以 k 的餘數 = 2
  }
  
  let tmp2 = null
  for(let i = 0; i < k; i++) { // [[1,2,3,4] , [5,6,7,8] , [9,10,11]]
    if (extraLength <= 0) extraLength = 0
    
    // 有沒有餘數，需不需要多一個
    let oneMore = 0
    if (extraLength > 0) {
      oneMore = 1
    }
    
    ret[i] = head
    for(let j = 0; j < partLength + oneMore; j++) {
      tmp2 = head
      if (head) {
        head = head.next
      }
    }
    extraLength = extraLength - 1
    // 把 tmp2 的下一個 next 截斷，然後進行下一個陣列的迴圈操作。
    if (tmp2) {
      console.log(tmp2.next)
      tmp2.next = null
    }
  }
  return ret
};

let node1 = new ListNode(1);
let node2 = new ListNode(2);
let node3 = new ListNode(3);
let node4 = new ListNode(4);
let node5 = new ListNode(5);
let node6 = new ListNode(6);
let node7 = new ListNode(7);
let node8 = new ListNode(8);
let node9 = new ListNode(9);
let node10 = new ListNode(10);
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
node5.next = node6;
node6.next = node7;
node7.next = node8;
node8.next = node9;
node9.next = node10;
console.log(splitListToParts(node1, 3));