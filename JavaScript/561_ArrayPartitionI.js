/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
  let res = 0;
  const sortedNums = nums.sort((a, b) => a - b);
  console.log(sortedNums)
  for (let i=0; i<sortedNums.length; i++) {
    if (i % 2 === 0) {
      res += sortedNums[i];
    }
  }
  return res;
};

console.log(arrayPairSum([1,4,3,2]))
console.log(arrayPairSum([6,2,6,5,1,2]))
console.log(arrayPairSum([6214, -2290, 2833, -7908]))