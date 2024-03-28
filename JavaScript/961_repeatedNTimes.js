/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 100 ms
 * Memory Usage: 45.4 MB
 * Big-O: O(n)
 * Idea: 直接去計算數字的出現次數
 */
var repeatedNTimes = function(nums) {
  const n = nums.length/2;
  let numsCount = {};
  for (let num of nums) {
    if (numsCount[num]) {
      numsCount[num] += 1;
      if (numsCount[num] === n) {
        return num;
      }
    } else {
      numsCount[num] = 1;
    }
  }
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 104 ms
 * Memory Usage: 41.7 MB
 * Big-O: O(n)
 * Idea: 依照題目特性，回傳的答案必定是唯一的重複數字，因此只需要去找到該重複的值即可
 */
var repeatedNTimes = function(nums) {
  let existSet = new Set();
  for (let i=0; i<nums.length; i++) {
    if (existSet.has(nums[i])) {
      return nums[i];
    } else {
      existSet.add(nums[i]);
    }
  }
  return -1;
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 84 ms
 * Memory Usage: 44.4 MB
 * Big-O: O(1)
 * Idea: 此解法也是腰劇題目特性，當我將所有的數字和減去不重複的數字和理應會得到答案乘上(n-1)
 * 方程式可以寫成 sum(nums) - sum(set(nums)) = (n-1)*result
 */
var repeatedNTimes = function(nums) {
  const sum = nums.reduce((acc, cur) => acc + cur, 0);
  const setSum = [...new Set(nums)].reduce((acc, cur) => acc + cur, 0);
  return (sum - setSum) / (nums.length/2 - 1);
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 
 * Memory Usage: 
 * Big-O: 
 * Idea: 鴿籠原理
 */
var repeatedNTimes = function(nums) {
  // 暴力解，當 len<=4
  if (nums.length <= 4) {
    for (let i=0; i<nums.length; i++) {
      for (let j=i+1; j<nums.length; j++) {
        if (nums[i] === nums[j]) {
          return nums[i]
        }
      }
    }
  }
  // len > 4 
  for (let i=0; i<nums.length-2; i++) {
    if ((nums[i] === nums[i+1]) || (nums[i] === nums[i+2])) {
      return nums[i];
    }
    if (nums[i+1] === nums[i+2]) {
      return nums[i+1];
    }
  }
  return -1;
};

console.log(repeatedNTimes([1,2,3,3]))
console.log(repeatedNTimes([2,1,2,5,3,2]))
console.log(repeatedNTimes([5,1,5,2,5,3,5,4]))
console.log(repeatedNTimes([0,1,4,8,9,4,4,4]))
