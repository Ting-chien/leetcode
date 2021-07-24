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