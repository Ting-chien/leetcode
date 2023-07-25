/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  // 先移除len<3的陣列
  if (nums.length < 3) {
    return [];
  }
  let res = [];
  nums.sort((a, b) => a - b);
  for (let i=0; i < nums.length; i++) {
    // 移除重複被檢查的值
    if (i > 0 && nums[i] === nums[i-1]) continue;
    let target = 0 - nums[i];
    //  進入雙指針解法
    let lpt = i + 1;
    let rpt = nums.length - 1;
    while (lpt < rpt) {
      if (nums[lpt] + nums[rpt] === target) {
        res.push([nums[i], nums[lpt], nums[rpt]]);
        // 移除重複被檢查的值
        while (lpt < rpt && nums[lpt] === nums[lpt+1]) lpt++;
        while (lpt < rpt && nums[rpt] === nums[rpt-1]) rpt--;
        // 往下一組數字檢查
        lpt ++;
        rpt --;
      } else if (nums[lpt] + nums[rpt] > target) {
        rpt --;
      } else {
        lpt ++;
      }
    }
  }
  return res;
};

console.log(threeSum([-1,0,1,2,-1,-4]))
console.log(threeSum([]))
console.log(threeSum([0]))
console.log(threeSum([0, 0, 0, 0]))