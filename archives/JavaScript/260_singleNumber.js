/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
  let result = [];
  let counts = new Map();
  for (let num of nums) {
    counts.set(num, (counts.get(num) || 0) + 1)
  }
  for (let entry of counts.entries()) {
    if (entry[1] === 1) {
      result.push(entry[0])
    }
  }
  return result;
};

console.log(singleNumber([1,2,1,3,2,5]))
console.log(singleNumber([-1,0]))
console.log(singleNumber([0,1]))