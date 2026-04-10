// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {

  // 宣告 naive head
  let head = new ListNode(0);
  // 宣告使用變數
  let current = head;
  let sum, carry = 0;

  while(l1 || l2 || carry > 0) {
    // 計算每一輪的總和
    sum = 0;
    if (l1 !== null) {
      sum += l1.val;
      l1 = l1.next;
    }
    if (l2 !== null) {
      sum += l2.val;
      l2 = l2.next;
    }
    // 將每一輪的總合放入 linked-list 中
    sum += carry;
    current.next = new ListNode(sum % 10);
    current = current.next;
    carry = sum > 9 ? 1 : 0;
  }

  return head.next;
};

console.log(addTwoNumbers([2, 4, 3], [5, 6, 4]))