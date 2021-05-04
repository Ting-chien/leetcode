/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  let l = 0;
  let r = nums.length - 1;
  while (l<=r) {
    let m = Math.round((l+r)/2);
    if (nums[m] === target) {
      return m;
    } else if (nums[m] > target) {
      r = m-1;
    } else {
      l = m+1;
    }
  }
  return -1;
};

console.log(search([-1,0,3,5,9,12], 9))
console.log(search([-1,0,3,5,9,12], 2))
console.log(search([5], 5))