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

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * 可以試試看 Binary Search 解法，可以"降低空間複雜度"
 * 依題目敘述，若陣列有100個數字，則數字在1~99，且只有一個數字重複
 * 因此從中切半看哪邊大於50的數量更多則可以知道重複的數字在哪邊
 */
var findDuplicate = function(nums) {
  let start = 0;
  let end = nums.length - 1;
  while (start+1 < end) {
    const mid = parseInt((end + start + 1) / 2)
    console.log(mid);
    let count = 0;
    for (let num of nums) {
      if (num > mid) count ++;
    }
    if (count > (end - mid)) {
      start = mid
    } else {
      end = mid
    }
  }
  return end;
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * 方法三：快慢指針（又稱龜兔賽跑）
 */
var findDuplicate = function(nums) {

};

console.log(findDuplicate([1,3,4,2,2]))
console.log(findDuplicate([3,1,3,4,2]))
console.log(findDuplicate([1,1]))
console.log(findDuplicate([1,1,2]))