/**
 * @param {number[]} nums
 * @return {number[]}
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

console.log(findDuplicates([4,3,2,7,8,2,3,1]))
console.log(findDuplicates([1,1,2]));
console.log(findDuplicates([1]))