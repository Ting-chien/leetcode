
// Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
  if (val === root.val) {
    return root;
  } else if (val < root.val) {
    if (!root.left) {
      return null;
    } else {
      return searchBST(root.left, val);
    }
  } else {
    if (!root.right) {
      return null;
    } else {
      return searchBST(root.right, val);
    }
  }
}

let node1 = new TreeNode(4);
let node2 = new TreeNode(2);
let node3 = new TreeNode(7);
let node4 = new TreeNode(1);
let node5 = new TreeNode(3);
node1.left = node2;
node1.right = node3;
node2.left = node4;
node2.right = node5;
console.log(searchBST(node1, 2))