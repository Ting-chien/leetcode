// /**
//  * @param {number[]} nums
//  * @param {number} target
//  * @return {number[][]}
//  */
// var fourSum = function(nums, target) {
//   // remove unwanted answer
//   if (nums.length < 4) {
//     return [];
//   }
//   // use two pointer solution
//   let res = [];
//   nums.sort((a, b) => a -b);
//   for (let i=0; i<nums.length-3; i++) {
//     if (i > 0 && nums[i] === nums[i-1]) continue;
//     for (let j=i+1; j<nums.length-2; j++) {
//       let remain = target - nums[i] - nums[j];
//       if (j > i+1 && nums[j] === nums[j-1]) continue;
//       let lpt = j + 1;
//       let rpt = nums.length - 1;
//       while (lpt < rpt) {
//         if (nums[lpt] + nums[rpt] === remain) {
//           res.push([nums[i], nums[j], nums[lpt], nums[rpt]]);
//           // 移除重複被檢查的值
//           while (lpt < rpt && nums[lpt] === nums[lpt+1]) lpt++;
//           while (lpt < rpt && nums[rpt] === nums[rpt-1]) rpt--;
//           // 往下一組數字檢查
//           lpt ++;
//           rpt --;
//         } else if (nums[lpt] + nums[rpt] > remain) {
//           rpt --;
//         } else {
//           lpt ++;
//         }
//       }      
//     }
//   }
//   return res;
// };

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 * 
 * 解題概念：利用"雙指針＋遞迴"的概念讓這題可以達到 nSum 的解題流程
 * 本題的時間複雜度就會是 O(N^n-1)，N 表示陣列長度，4Sum 就是 O(N^3)
 */
var fourSum = function(nums, target) {
  nums.sort((a, b) => a - b);
  let result = [];
  nSum(nums, 0, 4, target, [], result);
  return result;
};

function nSum(nums, start, n, target, current, result) {
  if (n === 2) {
    const subResult = twoSum(nums, start, target)
    for (let r of subResult) {
      result.push([...current, ...r])
    }
  } else {
    for (let i=start; i<nums.length; i++) {
      if (i > start && nums[i] === nums[i-1]) continue;
      current.push(nums[i]);
      nSum(nums, i+1, n-1, target-nums[i], current, result);
      current.pop();
    }
  }
}

function twoSum(nums, start, target) {
  let lpt = start;
  let rpt = nums.length - 1;
  let result = []
  while (lpt < rpt) {
    if (nums[lpt] + nums[rpt] === target) {
      result.push([nums[lpt], nums[rpt]]);
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
  return result;
}

console.log(fourSum([1,0,-1,0,-2,2], 0))
console.log(fourSum([2,2,2,2,2], 8))