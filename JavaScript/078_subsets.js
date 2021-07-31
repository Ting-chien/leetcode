/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    // backtracking function
    const backtrack = (first = 0, curr = []) => {
        // base case
        if (curr.length === i) {
            result.push([...curr]);
            return
        }
        // general case
        for (let j=first; j<nums.length; j++) {
            curr.push(nums[j]);
            backtrack(j+1, curr);
            curr.pop();
        }
    }
    // main
    const n = nums.length;
    const result = [];
    for (var i=0; i<nums.length+1; i++) {
        backtrack();
    }
    return result;
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    // 建立一組回傳陣列來收集所有 subsets
    let result = [[]];
    // 每次將陣列元素乘以2，增加一種可能性
    nums.forEach(num => {
        let copyResult = JSON.parse(JSON.stringify(result));
        copyResult.forEach(ele => {
            ele.push(num);
        })
        result.push(...copyResult)
    });
    return result;
};