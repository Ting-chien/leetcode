/**
 * @param {number[]} nums
 * @return {number[]}
 * 
 * 
 * Runtime: 4584 ms
 * Memory: 49 MB
 */
var findDuplicates = function(nums) {
  let collection = [];
  let res = [...nums];
  for (let i=0; i<=nums.length; i++) {
    let temp = res.shift();
    if (collection.includes(temp)) {
      res.push(temp);
    } else {
      collection.push(temp);
    }
  }
  return res;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 * 
 * 助教解法一：排序
 * 先將陣列排序，再依序比對是否有連續兩個值是一樣的
 * 
 * Runtime: 172 ms
 * Memory: 48.3 MB
 * */
var findDuplicates = function(nums) {
  let res = [];
  const sortedNums = nums.sort();
  for (let i=0; i<sortedNums.length; i++) {
    if (i>0 && sortedNums[i] === sortedNums[i-1]) res.push(sortedNums[i]);
  }
  return res;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 * 
 * 解法二：儲存與比對
 * 先用陣列來儲存所有數字，在用迴圈跑過陣列一次看是否有儲存過
 * 
 * Runtime: 136 ms
 * Memory: 49.3 MB
 */
var findDuplicates = function(nums) {
  let res = [];
  let recordNums = {};
  for (let i=0; i<nums.length; i++) {
    if (recordNums[nums[i]] === 1) {
      res.push(nums[i]);
    } else {
      recordNums[nums[i]] = 1;
    }
  }
  return res;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 * 
 * 解法三：解法貳的變化版
 * 利用題目中說明重複的數字"最多出現兩次"，且數字介於[1,nums.length()]之間的特性來解題
 * 
 * Runtime: 112 ms
 * Memory: 46.2 MB
 */
 var findDuplicates = function(nums) {
  let res = [];
  for (let i=0; i<nums.length; i++) {
    const n = Math.abs(nums[i]);
    const index = n - 1;
    if (nums[index] < 0) {
      res.push(n);
    } else {
      nums[index] *= -1;
    }
  }
  return res;
};

console.log(findDuplicates([4,3,2,7,8,2,3,1]))
console.log(findDuplicates([1,1,2]));
console.log(findDuplicates([1]))