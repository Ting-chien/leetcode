
/**
 * Definition for a binary tree node.
 * @param {number} val 
 * @param {TreeNode} left 
 * @param {TreeNode} right 
 */
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * Stack + DFS
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {

    if (root == null) return []

    let stack = [root]
    let value = []

    while (stack.length > 0) {
        let node = stack.pop()
        value.push(node.val)
        if (node.right != null) {
            stack.push(node.right)
        }
        if (node.left != null) {
            stack.push(node.left)
        }
    }

    return value;
};

/**
 * DFS + recursion
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {

    const traverse = (node) => {
        if (!node) return
        value.push(node.val)
        traverse(node.left)
        traverse(node.right)
    }

    let value = []
    traverse(root)
    return value;

};

/**
 * DFS + recursion (advanced)
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {

    // 透過解構賦值來減少代碼行數
    function traverse(node) {
        if (!node) return [];
        return [node.val, ...traverse(node.left), ...traverse(node.right)];
    }

    return traverse(root)

};

/**
 * DFS + recursion (advanced)
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {

    // 避免宣告額外的函數來解決問題
    if (!root) return [];
    let result = [root.val];
    result.push(...preorderTraversal(root.left))
    result.push(...preorderTraversal(root.right))
    return result;

};

let node1 = new TreeNode(1)
let node2 = new TreeNode(4)
let node3 = new TreeNode(3)
let node4 = new TreeNode(2)
node1.left = node2
node1.right = node3
node2.left = node4
console.log(preorderTraversal(node1))