/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {

    // 事前檢查，如果頭尾無法前進直接回傳-
    if ((grid[0][0] != 0) || (grid[grid.length-1][grid.length-1] != 0)) return -1
    // 如果只有一格則直接回傳1
    if (grid.length == 1) return 1

    // 宣告需使用的變數、儲存格
    let num = grid.length
    let nextSteps = [[0, 0, 1]]
    let visited = [[0, 0]]
    let steps = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

    // 當nextStep中有待訪問座標，則對該座標進行嘗試
    while (nextSteps.length > 0) {
        let row, col, distance;
        [row, col, distance] = nextSteps.shift()
        // console.log(`row = ${row}, col = ${col}, num = ${num}, distance = ${distance}`)
        // 如果是終點，直接回傳結果
        if ((row == num-1) && (col == num-1)) return distance
        // 造訪八個前進方向，並判斷是否已觸碰邊界條件
        for (let step of steps) {
            let nextRow = row + step[0]
            let nextCol = col + step[1]
            if (!((nextRow >= 0) && (nextCol >= 0) && (nextRow < num) && (nextCol < num) && (grid[nextRow][nextCol] == 0))) {
                continue;
            }
            let nextStep = [nextRow, nextCol]
            let isVisited = visited.some(x => nextStep.every((v, i) => v === x[i]))
            if (!(isVisited)) {
                nextSteps.push([nextRow, nextCol, distance+1])
                visited.push([nextRow, nextCol])
            }
        }
        console.log("+"*50)
    }

    return -1;
    
};

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {

    // 事前檢查，如果頭尾無法前進直接回傳-
    if ((grid[0][0] != 0) || (grid[grid.length-1][grid.length-1] != 0)) return -1
    // 如果只有一格則直接回傳1
    if (grid.length == 1) return 1

    // 宣告需使用的變數、儲存格
    let num = grid.length
    let nextSteps = [[0, 0, 1]]
    let visited = {}
    visited[[0, 0]] = 1
    let steps = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

    // 當nextStep中有待訪問座標，則對該座標進行嘗試
    while (nextSteps.length > 0) {
        let row, col, distance;
        [row, col, distance] = nextSteps.shift()
        // console.log(`row = ${row}, col = ${col}, num = ${num}, distance = ${distance}`)
        // 如果是終點，直接回傳結果
        if ((row == num-1) && (col == num-1)) return distance
        // 造訪八個前進方向，並判斷是否已觸碰邊界條件
        for (let step of steps) {
            let nextRow = row + step[0]
            let nextCol = col + step[1]
            if (!((nextRow >= 0) && (nextCol >= 0) && (nextRow < num) && (nextCol < num) && (grid[nextRow][nextCol] == 0))) {
                continue;
            }
            if (!(visited.hasOwnProperty([nextRow, nextCol]))) {
                nextSteps.push([nextRow, nextCol, distance+1])
                visited[[nextRow, nextCol]] = 1
            }
        }
        console.log("+"*50)
    }

    return -1;
    
};

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {

    // 事前檢查，如果頭尾無法前進直接回傳-
    if ((grid[0][0] != 0) || (grid[grid.length-1][grid.length-1] != 0)) return -1
    // 如果只有一格則直接回傳1
    if (grid.length == 1) return 1

    // 宣告需使用的變數、儲存格
    let num = grid.length
    let nextSteps = [[0, 0]]
    let distance = 1
    let steps = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

    // 當nextStep中有待訪問座標，則對該座標進行嘗試
    while (nextSteps.length > 0) {
        let numOfSteps = nextSteps.length;
        for (let i=0; i<numOfSteps; i++) {
            let row, col;
            [row, col] = nextSteps.shift()
            // 如果是終點，直接回傳結果
            if ((row == num-1) && (col == num-1)) return distance
            // 造訪八個前進方向，並判斷是否已觸碰邊界條件
            for (let step of steps) {
                let nextRow = row + step[0]
                let nextCol = col + step[1]
                if (((nextRow >= 0) && (nextCol >= 0) && (nextRow < num) && (nextCol < num) && (grid[nextRow][nextCol] == 0))) {
                    grid[nextRow][nextCol] = 1
                    nextSteps.push([nextRow, nextCol, distance+1])
                }
            }
        }
        distance += 1
    }

    return -1;
};

console.log(shortestPathBinaryMatrix([[0,1],[1,0]]))
console.log(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
console.log(shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))