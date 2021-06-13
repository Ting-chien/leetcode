/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 92 ms
 * Memory Usage: 40.5 MB
 * Big-O: O(n)
 */
var removeDuplicates = function(nums) {
  let isRepeated = false;
  for (let i=0; i<nums.length; i++) {
    // 如果數字已經重複兩次以上，則略過不計算
    if (isRepeated && nums[i] === nums[i-1]) {
      nums.splice(i, 1);
      i -= 1;
    }
    // 如果數字還未重複過但和前一個一樣，則isRepeated = true
    if (nums[i] === nums[i-1]) {
      isRepeated = true;
    } else {
      isRepeated = false;
    }
  }
  return nums.length;
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 116 ms
 * Memory Usage: 40.6 MB
 * Big-O: unknown
 * Idea: 快慢指針＋計數器（血頭是最後的寫入），慢指針負責寫，快指針負責讀
 */
var removeDuplicates = function(nums) {
  // 因為題目表示相同的數字最多出現兩次，因此先過濾掉length<=2的陣列
  if (nums.length <= 2) {
    return nums.length;
  }
  // 建立快慢指針和計數器
  let slow = 0; // 寫頭
  let fast = 1; // 讀頭
  let count = 1;
  while (fast < nums.length) {
    // 兩指針的數字不同，則將獨到的數字寫在讀投下一個位置並歸零計數器
    if (nums[slow] !== nums[fast]) {
      nums[++slow] = nums[fast];
      count = 1;
    } else {
      // 兩指針的數字相同，則查看計數器是否已達上限
      if (count < 2) {
        // 計數器未達兩次則寫頭繼續往下紀錄，否則寫頭不動
        nums[++slow] = nums[fast];
        count ++;
      }
    }
    fast ++;
  }
  return slow + 1;
};

/**
 * @param {number[]} nums
 * @return {number}
 * 
 * Runtime: 132 ms	
 * Memory Usage: 40.5 MB
 * Big-O: unknown
 * Idea: 快慢指針（寫頭可直接寫入），慢指針負責寫，快指針負責讀
 */
var removeDuplicates = function(nums) {
  // 因為題目表示相同的數字最多出現兩次，因此先過濾掉length<=2的陣列
  if (nums.length <= 2) {
    return nums.length;
  }
  // 依據題目的需求建立慢指針 (countMax = 2)
  let slow = 2;
  for (let fast = 2; fast < nums.length; fast++) {
    if (nums[slow-2] !== nums[fast]) {
      nums[slow] = nums[fast];
      slow ++;
    }
  }
  return slow;
};

console.log(removeDuplicates([1,1,1,2,2,3]))
console.log(removeDuplicates([0,0,1,1,1,1,2,3,3]))