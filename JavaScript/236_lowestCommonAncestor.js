/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 * => use stack
 */
var lowestCommonAncestor = function(root, p, q) {
    // 建立經過遍歷的 nodes
    const stack = [root];
    // 建立尋找 p, q 路徑上的 nodes
    const parent = new Map().set(root, null);
    // 對 binary tree 遍歷直到找到 p, q
    while (!parent.has(p) || !parent.has(q)) {
        const node = stack.pop();
        // 檢查是否可繼續往左遍歷
        if (node.left) {
            parent.set(node.left, node);
            stack.push(node.left);
        }
        // 檢查是否可繼續往右遍歷
        if (node.right) {
            parent.set(node.right, node);
            stack.push(node.right);
        }
    }
    // 建立一個 set 來儲存 p 路徑上所有的 node
    let ancestors = new Set();
    while (p) {
        ancestors.add(p);
        p = parent.get(p);
    }
    // 在 ancestor 中尋找是否有符合 q 或 q.ancestor 的節點
    while (!(ancestors.has(q))) {
        q = parent.get(q);
    }
    return q;
};

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 * => use recursion
 */
var lowestCommonAncestor = function(root, p, q) {
    // 如果 root = null 則直接回傳 null
    if (!root) return null;
    // 如果 q 或 q 為 root 則 LCA = root
    if (p === root || q === root) return root;
    // 向左或向右遍歷
    const left = lowestCommonAncestor(root.left, p, q);
    const right = lowestCommonAncestor(root.right, p, q);
    if (left && right) {
        return root;
    } else if (left) {
        return left;
    } else {
        return right;
    }
};