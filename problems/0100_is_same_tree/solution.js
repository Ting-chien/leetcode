// Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

let node1 = new TreeNode(1);
let node2 = new TreeNode(2);
// let node3 = new TreeNode(3);
node1.left = node2;
// node1.right = node3;

let copyNode1 = new TreeNode(1);
let copyNode2 = new TreeNode(2);
copyNode1.left = copyNode2;

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
  if (p && q && p.val === q.val) {
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
  } else if (!p && !q) {
    return true
  } else {
    return false
  }
};

console.log(isSameTree(node1, copyNode1))