
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

let node1 = new TreeNode(1)
let node2 = new TreeNode(2)
let node3 = new TreeNode(3)
node1.left = node2;
node1.right = node3;

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function(root) {
    let maxSum = -Number.MAX_VALUE;
    function postOrder(root) {
        if (!root) return 0;
        // 計算 root 左右兩側的最大總和，若小於 0 則直接捨棄
        let left = Math.max(0, postOrder(root.left));
        let right = Math.max(0, postOrder(root.right));
        maxSum = Math.max(maxSum, root.val + left + right);
        return root.val + Math.max(left, right);
    };
    postOrder(root)
    return maxSum;
};

console.log(maxPathSum(node1))