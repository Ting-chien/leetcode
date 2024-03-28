
/**
 * Definition for singly-linked list.
 * @param {number} val 
 * @param {ListNode} next 
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * 此題為21. Merge Two Sorted Lists延伸，透過先拆分在合併來實作merge sort
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    
    // 先確認是否可往下拆解
    if (!head || !head.next) {
        return head;
    }
    
    // 確認可往下拆解list後將list拆成一半
    let mid = getMidNode(head)
    let nMid = mid.next
    mid.next = null
    
    // 將排序後的左右兩list合併並排序
    return mergeTwoLists(sortList(head), sortList(nMid))
};

var getMidNode = function(head) {

    // 若長度不足，則直接回傳head
    if (!head || !head.next) {
        return head;
    }

    // 透過快慢指針來找出中間點
    let slow = head;
    let fast = head;
    while (fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
}

var mergeTwoLists = function(l1, l2) {

    // 設定終止條件，如果l1,l2都為空，那就結束recursive
    if (!l1 && !l2) {
        return null
    }

    // 若其中一個list有值，則依序判斷
    let curr = null
    if (!l1) {
        curr = l2
        l2 = l2.next
    } else if (!l2) {
        curr = l1
        l1 = l1.next
    } else if (l1.val >= l2.val) {
        curr = l2
        l2 = l2.next
    } else {
        curr = l1
        l1 = l1.next
    }

    curr.next = mergeTwoLists(l1, l2)

    return curr
};

let node1 = new ListNode(4)
let node2 = new ListNode(2)
let node3 = new ListNode(1)
let node4 = new ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
console.log(sortList(node1))