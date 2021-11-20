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
 * 解法一，主要概念是透過dummy head的概念來精簡解題
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {

    // 建立一個dummy head來承接l1,l2結果
    let vHead = new ListNode(0)
    let curr = vHead

    while (l1 || l2) {
        // 宣告一個node來作為curr下一個節點
        let node = null
        // 比較l1,l2大小或是否存在
        if (!l1) {
            node = l2
            l2 = l2.next
        } else if (!l2) {
            node = l1
            l1 = l1.next
        } else if (l1.val >= l2.val) {
            node = l2
            l2 = l2.next
        } else if (l1.val < l2.val) {
            node = l1
            l1 = l1.next
        }
        // 將curr往下一個節點移
        curr.next = node
        curr = node
    }

    return vHead.next
};

/**
 * 前一個解法的延伸，思考若其中一組list已經為空，那是否直接將剩餘的list接至curr後
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {

    // 建立一個dummy head來承接l1,l2結果
    let vHead = new ListNode(0)
    let curr = vHead

    while (l1 && l2) {
        // 宣告一個node來作為curr下一個節點
        let node = null
        // 比較l1,l2大小或是否存在
        if (l1.val >= l2.val) {
            node = l2
            l2 = l2.next
        } else {
            node = l1
            l1 = l1.next
        }
        // 將curr往下一個節點移
        curr.next = node
        curr = node
    }
    // 將剩餘的list直接接至curr後
    curr.next = l1 || l2

    return vHead.next
};

/**
 * 和前兩個解法不同，解法弎改用recursive取代while迴圈
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {

    // 設定終止條件，如果l1,l2都為空，那就結束recursive
    if (!l1 && !l2) {
        return
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

let node1 = new ListNode(1)
let node2 = new ListNode(2)
let node3 = new ListNode(4)
node1.next = node2
node2.next = node3

let node4 = new ListNode(1)
let node5 = new ListNode(3)
let node6 = new ListNode(4)
node4.next = node5
node5.next = node6

console.log(mergeTwoLists(node1, node4))