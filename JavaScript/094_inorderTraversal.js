
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

let node1 = new TreeNode(1);
let node2 = new TreeNode(2);
let node3 = new TreeNode(3);
node1.right = node2;
node2.left = node3;

// /**
//  * @param {TreeNode} root
//  * @return {number[]}
//  */
// var inorderTraversal = function(root) {
//   if (!root) return [];
//   const result = [];
//   if (root.left) {
//     result.push(...inorderTraversal(root.left))
//   }
//   result.push(root.val)
//   if (root.right) {
//     result.push(...inorderTraversal(root.right))
//   }
//   return result;
// };

// /**
//  * @param {TreeNode} root
//  * @return {number[]}
//  */
// var inorderTraversal = function(root) {
//   let result = [];
//   dfs(root);

//   function dfs(root) {
//     if (root) {
//       dfs(root.left)
//       result.push(root.val)
//       dfs(root.right)
//     }
//   }

//   return result;
// };

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
  let stack = [];
  let result = [];
  let current = root;
  while (stack.length > 0 || current) {
    while (current) {
      stack.push(current);
      current = current.left;
    }
    current = stack.pop();
    console.log(current)
    result.push(current.val);
    current = current.right;
  }
  return result;
};

console.log(inorderTraversal(node1));