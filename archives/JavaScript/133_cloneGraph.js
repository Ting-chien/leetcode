
/**
 * Definition for a Node.
 * @param {number} val 
 * @param {Node} neighbors 
 */
function Node(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
};

/**
 * 規則一：graph必從node.val=1開始，並向上遞增
 * 規則二：graph沒有無限迴圈的情況
 * 方法一：queue+while loop
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node) {

    if (!node) return node;

    // 建立一個map來記錄已走過的節點
    let visited = new Map();

    // bfs起手式，先建立一queue並將node放入
    let queue = [node];
    visited.set(node, (new Node(node.val, [])));

    // bfs標準流程，當queue裡面仍有值時不斷地去將節點讀出
    while (queue.length > 0) {
        let curr = queue.shift();
        for (let neighbor of curr.neighbors) {
            if (!visited.has(neighbor)) {
                visited.set(neighbor, (new Node(neighbor.val, [])))
                queue.push(neighbor)
            }
            visited.get(curr).neighbors.push(visited.get(neighbor))
        }
    }

    return visited.get(node);

};

/**
 * 方法二：使用dfs(recursive)
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node) {

    // 檢查graph是否有節點
    if (!node) return node;

    // 創建一個map來儲存造訪過的節點
    let visited = new Map();

    const dfs = (node) => {

        // 終止條件一：不存在欲查找的節點
        if (!node) return node;

        // 終止條件二：如果visited中已存在節點
        if (visited.has(node)) return visited.get(node);

        // 新建一節點加入visited中，並切將neighbors也拷貝一份加入
        let copyNode = new Node(node.val, []);
        visited.set(node, copyNode)
        for (let neighbor of node.neighbors) {
            copyNode.neighbors.push(dfs(neighbor))
        }

        return copyNode;
    }

    return dfs(node);
};


let node1 = new Node(1, [])
let node2 = new Node(2, [])
let node3 = new Node(3, [])
let node4 = new Node(4, [])
node1.neighbors.push(node2)
node1.neighbors.push(node4)
node2.neighbors.push(node1)
node2.neighbors.push(node3)
node3.neighbors.push(node2)
node3.neighbors.push(node4)
node4.neighbors.push(node3)
node4.neighbors.push(node1)
console.log(cloneGraph(node1).neighbors)