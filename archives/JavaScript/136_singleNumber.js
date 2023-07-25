/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 100 ms
 * Memory Usage: 47.4 MB
 * Big-O: O(n)
 */
var singleNumber = function(nums) {
  let numsCount = {};
  for (let num of nums) {
    if (numsCount[num]) {
      numsCount[num] += 1;
    } else {
      numsCount[num] = 1;
    }
  }
  for (let entry of Object.entries(numsCount)) {
    if (entry[1] === 1) {
      return entry[0]
    }
  }
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 128 ms
 * Memory Usage: 43.2 MB
 * Big-O: O(n)
 * Idea: 利用 Set() 來儲存＆移除相異的數字
 */
var singleNumber = function(nums) {
  const existSet = new Set();
  for (let num of nums) {
    if (!existSet.has(num)) {
      existSet.add(num);
    } else {
      existSet.delete(num);
    }
  }
  for (let num of existSet) {
    return num;
  }
  return -1;
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 84 ms
 * Memory Usage: 41.9 MB
 * Big-O: O(n)
 * Idea: 利用題目特性將 2*sum(set(nums)) - sum(nums)
 */
var singleNumber = function(nums) {
  const sum = nums.reduce((acc, cur) => acc + cur, 0);
  const doubleSetSum = 2*[...new Set(nums)].reduce((acc, cur) => acc + cur, 0);
  return doubleSetSum - sum;
}

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 84 ms
 * Memory Usage: 41.9 MB
 * Big-O: O(n)
 * Idea: XOR
 */
var singleNumber = function(nums) {
  let sum = 0;
  for (let num of nums) {
    sum ^= num;
  }
  return sum;
}

console.log(singleNumber([2,2,1]))
console.log(singleNumber([4,1,2,1,2]))
console.log(singleNumber([1]))