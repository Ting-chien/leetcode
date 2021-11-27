
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
 * 方法一：使用recursive+BFS
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    
    if (!root) return []
    
    let result = []

    function traverse(node, level) {

        if (!node) return

        if (!result[level]) {
            result[level] = [node.val]
        } else {
            result[level].push(node.val)
        }

        traverse(node.left, level+1)
        traverse(node.right, level+1)
    }

    traverse(root, 0);
    return result;
};

/**
 * 方法一（延伸）：將array換成object
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    
    if (!root) return []
    
    let result = {}

    function traverse(node, level) {

        if (!node) return

        if (result.hasOwnProperty(level)) {
            result[level].push(node.val)
        } else {
            result[level] = [node.val]
        }

        traverse(node.left, level+1)
        traverse(node.right, level+1)
    }

    traverse(root, 0);
    return Object.values(result);
};

/**
 * 方法二：在函數中加入一些參數入口來使recursive只需使用一個function
 * @param {TreeNode} root
 * @return {number[][]}
 */
function levelOrder(root, level=0, result=[]) {
    if (!root) return [];
    result[level] = result[level] || [];
    result[level].push(root.val);
    levelOrder(root.left, level+1, result);
    levelOrder(root.right, level+1, result);
    return result;
}

/**
 * 方法弎：使用傳統Queue+BFS解題，要注意因為答案須將不同層的node分開，所以需多上一層nodeLevel的處理
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    
    if (!root) return []

    let res = [], queue = [root, null]
    let levelNodes = []

    while (queue.length > 0) {
        let node = queue.shift()
        if (node) {
            levelNodes.push(node.val)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        } else {
            res.push(levelNodes)
            levelNodes = []
            if (queue.length) queue.push(null)
        }
    }

    return res;
    
};

// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]
node1 = new TreeNode(3)
node2 = new TreeNode(9)
node3 = new TreeNode(20)
node4 = new TreeNode(15)
node5 = new TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
console.log(levelOrder(node1))