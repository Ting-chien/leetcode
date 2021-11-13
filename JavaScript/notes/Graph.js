function bfs(root) {

    let queue = [root]
    let values = []

    while (queue.length > 0) {
        let node = queue.shift()
        values.push(node.value)
        if (node.left) {
            queue.push(node.left)
        }
        if (node.right) {
            queue.push(node.right)
        }
    }

    return values

}

function dfs(root) {

    let stack = [root]
    let values = []

    while (stack.length > 0) {
        let node = stack.pop()
        values.push(node.value)
        // 從右邊節點遍歷代表先看樹的左側
        if (node.right) {
            stack.push(node.right)
        }
        if (node.left) {
            stack.push(node.left)
        }
    }

    return values
    
}