/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * key: None, naive solution.
 * time complexity: O(n^2)
 * runtime: 96 ms
 * memory: 39 MB
 */
var twoSum = function(nums, target) {
  for (let i=0; i<nums.length; i++) {
    const remain = target - nums[i];
    for (let j=i+1; j<nums.length; j++) {
      if (nums[j] === remain) {
        return [i, j];
      }
    }
  }
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * key: hash map
 * time complexity: O(n)
 * runtime: 80 ms
 * memory: 39.4 MB
 */
var twoSum = function(nums, target) {
  let map = {};
  for (let i=0; i<nums.length; i++) {
    const remain = target - nums[i];
    if (remain in map) {
      return [map[remain], i];
    }
    map[nums[i]] = i;
  }
};

console.log(twoSum([2,7,11,15], 9))
console.log(twoSum([3,2,4], 6))
console.log(twoSum([3,3], 6))