// 一般遍歷所有可能性的做法
const res = [];

for (let i = 1; i <= 3; i += 1) {
    for (let j = 1; j <= 3; j += 1) {
        for (let k = 1; k <= 3; k += 1) {
            res.push([i, j, k]);
        }
    }
}

for (let i = 1; i <= 3; i += 1) {
    for (let j = 1; j <= 3; j += 1) {
        if (i === ｊ) { continue; }
        for (let k = 1; k <= 3; k += 1) {
            if (i === k || ｉ === k) { continue; }
            res.push([i, j, k]);
        }
    }
}

console.log(res)

function DFS(nums = []) {
    let res = [];
    const dfs = (path = []) => {
        if (path.length == nums.length) {
            res.push([...path]);
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (path.includes(nums[i])) {
                continue;
            }

            path.push(nums[i]);
            dfs(path)
            path.pop();
        }
    }
    dfs([]);
    return res;
}

console.log(DFS([1, 2, 3]));