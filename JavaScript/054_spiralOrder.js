/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    
    let top = 0
    let left = 0
    let right = matrix[0].length
    let buttom = matrix.length
    let maxLength = matrix.length*matrix[0].length
    let res = []

    while (top < buttom && left < right) {
        for (let i=left; i<right; i++) {
            res.length < maxLength && res.push(matrix[top][i])
        }
        top += 1
        for (let i=top; i<buttom; i++) {
            res.length < maxLength && res.push(matrix[i][right-1])
        }
        right -= 1
        for (let i=right-1; i>left-1; i--) {
            res.length < maxLength && res.push(matrix[buttom-1][i])
        }
        buttom -= 1
        for (let i=buttom-1; i>top-1; i--) {
            res.length < maxLength && res.push(matrix[i][left])
        }
        left += 1
    }

    return res
};

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
 var spiralOrder = function(matrix) {
    
    if (!matrix || !matrix[0]) {
        return [];
    }

    let direction = 0;
    let acceleration = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    let row = 0
    let col = -1
    let len = [matrix[0].length, matrix.length - 1]
    let result = []

    while (len[direction%2]) {
        for (let i=0; i<len[direction%2]; i++) {
            row += acceleration[direction][0]
            col += acceleration[direction][1]
            result.push(matrix[row][col])
        }
        len[direction%2] --;
        direction = (direction+1) % 4
    }
    
    return result
};

console.log(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))