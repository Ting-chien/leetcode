/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {

    let checked = new Set()
    let preMap = new Map()

    // Step1.將prerequisites轉為HashMap以方便後續查找
    for (let pre of prerequisites) {
        const take = pre[0]
        const need = pre[1]
        if (preMap.has(take)) {
            let preList = preMap.get(take)
            preList.push(need)
            preMap.set(take, preList)
        } else {
            preMap.set(take, [need])
        }
    }
    console.log(preMap)

    // Step2.依序檢查每堂課是否可被選取
    let checking = new Set()
    for (let i=0; i<numCourses; i++) {
        checking.clear()
        if (!validate(numCourses, i, preMap, checked, checking)) {
            return false
        }
    }

    return true
    
};

/**
 * 透過dfs逐一向下遍歷來確認該課程是否可被選修
 * @param {number} numCourses 總共要選修的課堂數
 * @param {number} target 待確認的課
 * @param {Map} preMap 課表
 * @param {number[]} checked 已確認可修的課
 * @param {number[]} checking 還在確認是否可修的課
 */
var validate = function(numCourses, target, preMap, checked, checking) {

    // 確認待檢查的課程是否已通過或不需要先修課
    if (checked.has(target) || !preMap.has(target)) {
        return true
    }
    // 如果該課程還在確認中，則先不通過檢查
    if (checking.has(target)) {
        return false
    }

    // 開始執行檢查動作
    checking.add(target)
    let preList = preMap.get(target)
    for (let pre of preList) {
        if (!validate(numCourses, pre, preMap, checked, checking)) {
            return false
        }
    }
    checked.add(target)
    return true
}


/**
 * 解法貳：使用bfs（拓普排序Topological Sort的延伸）
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {

    // Step1.先建立每堂課之間"邊(edge)"的關係，0代表該課程沒有必要先修課
    let inBounds = Array(numCourses).fill(0)
    let preMap = new Map()
    for (let pre of prerequisites) {
        let take = pre[0]
        let need = pre[1]
        inBounds[need]++
        if (preMap.has(take)) {
            let preList = [...preMap.get(take)]
            preList.push(need)
            preMap.set(take, preList)
        } else {
            preMap.set(take, [need])
        }
    }
    console.log(`inBounds = ${inBounds}`)
    console.log(`preMap = `, preMap)

    // Step2.建立queue，從第一個可修的課(inBound=0)開始放入
    let queue = []
    for (let i=0; i<inBounds.length; i++) {
        if (inBounds[i] == 0) {
            queue.push(i)
        }
    }

    // Step3.逐一遍歷queue內部所有的節點
    while (queue.length > 0) {
        let course = queue.shift()
        if (!preMap.has(course)) { preMap.set(course, []) }
        for (let pre of preMap.get(course)) {
            inBounds[pre]--
            if (inBounds[pre] == 0) {
                queue.push(pre)
            }
        }
    }

    // Step4.檢查是否所有課都已經可被選修
    for (let inBound of inBounds) {
        if (inBound > 0) {
            return false
        }
    }

    return true

}

console.log(canFinish(2, [[1,0]]))
console.log(canFinish(2, [[1,0],[0,1]]))
console.log(canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))