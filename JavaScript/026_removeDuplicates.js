/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let slow = 0
  let fast = slow + 1
  while (fast < nums.length) {
    if (nums[fast] !== nums[slow]) {
      nums[slow+1] = nums[fast];
      slow ++;
    }
    fast ++;
  }
  return slow + 1;
};

console.log(removeDuplicates([1,1,2]))
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))