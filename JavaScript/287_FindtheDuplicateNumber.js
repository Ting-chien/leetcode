/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
  let exist = new Set();
  for (let num of nums) {
    if (exist.has(num)) {
      return num;
    }
    exist.add(num)
  }    
};

console.log(findDuplicate([1,3,4,2,2]))
console.log(findDuplicate([3,1,3,4,2]))
console.log(findDuplicate([1,1]))
console.log(findDuplicate([1,1,2]))