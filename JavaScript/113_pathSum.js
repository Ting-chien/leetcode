
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {

    const result = [];

    var preOrder = (root, target, curr=[]) => {
        console.log(curr)
        // base condition
        if (!root) return
        if (target === root.val && !root.left && !root.right) {
            result.push([...curr, root.val])
            return
        }
        // general condition
        curr.push(root.val)
        preOrder(root.left, target - root.val, curr)
        preOrder(root.right, target - root.val, curr)
        curr.pop()
    }

    preOrder(root, targetSum)

    return result;
};

/**
 * DFS => stack
 * BFS => queue
 */
var pathSum = function(root, targetSum) {
    if (!root) return []
    const result = [];

    let queue = [[root, [root.val], root.val]]
    while(queue.length) {
        const [root, tmpResult, sum] = queue.shift()
        if (sum === targetSum && !root.left && !root.right) {
            result.push(tmpResult)
        }
        if (root.left) {
            queue.push([root.left, [...tmpResult, root.left.val], sum + root.left.val])
        }
        if (root.right) {
            queue.push([root.right, [...tmpResult, root.right.val], sum + root.right.val])
        }
    }

    return result
};
var pathSum = function(root, sum) {
    if (!root) return []
    const results = []
    const queue = [[root, [root.val], root.val]]
    while (queue.length) {
        const [node, arr, cur] = queue.shift()
        if (!node.left && !node.right && cur === sum) {
            results.push(arr)
        }
        if (node.left) {
            queue.push([node.left, [...arr, node.left.val], cur + node.left.val])
        } 
        if (node.right) {
            queue.push([node.right, [...arr, node.right.val], cur + node.right.val])
        }
    }
    return results
}



let node1 = new TreeNode(1)
let node2 = new TreeNode(2)
let node3 = new TreeNode(3)
node1.left = node2
node1.right = node3

console.log(pathSum(node1, 3))