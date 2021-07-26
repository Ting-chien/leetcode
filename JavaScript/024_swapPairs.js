
/**
 * @param {Number} val 
 * @param {ListNode} next 
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    if (!head || !head.next) {
        return head;
    } else if (head.next && !head.next.next) {
        const next = head.next;
        next.next = head;
        head.next = null;
        return next;
    } else {
        const next = head.next;
        head.next = swapPairs(head.next.next);
        next.next = head;
        return next;
    }
};
var swapPairs = function(head) {
    let thead = new ListNode(0); // 0
    thead.next = head; // 0 -> 1
    let tmp = thead; // 0
    while(tmp.next != null && tmp.next.next != null){
        let start = tmp.next; // 1
        let end = start.next; // 2
        tmp.next = end; // 0 -> 2
        start.next = end.next; // 1 -> 3
        end.next = start; // 2 -> 1
        tmp = start;
    }
    return thead.next;
};
var swapPairs = function(head) {
    if (!head || !head.next) return head;
    const next = head.next;
    head.next = swapPairs(head.next.next);
    next.next = head;
    return next;
    // destruct operator
    // let [fst, snd] = [head, head.next];
    // [fst.next, snd.next] = [swapPairs(snd.next), fst];
    // return snd;
};

const node1 = new ListNode(1);
const node2 = new ListNode(2);
const node3 = new ListNode(3);
const node4 = new ListNode(4);
node1.next = node2;
node2.next = node3;
node3.next = node4;
console.log(swapPairs(node1));