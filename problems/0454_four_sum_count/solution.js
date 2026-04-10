/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 * 
 * 幹O(n^4)測資最好會過，直接Time Limit Exceeded
 */
// var fourSumCount = function(nums1, nums2, nums3, nums4) {
//   let count = 0;
//   for (let num1 of nums1) {
//     for (let num2 of nums2) {
//       for (let num3 of nums3) {
//         for (let num4 of nums4) {
//           if ((num1 + num2 + num3 + num4) === 0) count++;
//         }
//       }
//     }
//   }
//   return count;
// };

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 * 
 * 助教在這題將四個回圈拆成兩個回圈，並用Map()來存回圈的結果，相對的使用的記憶體空間就大一些
 */
var fourSumCount = function(nums1, nums2, nums3, nums4) {
  let AB = new Map();
  for (let a of nums1) {
    for (let b of nums2) {
      AB.set(a+b, (AB.get(a+b) || 0) + 1)
    }
  }
  let count = 0;
  for (let c of nums3) {
    for (let d of nums4) {
      const target = -c - d;
      count += AB.get(target) || 0;
    }
  }
  return count;
};


console.log(fourSumCount([1,2], [-2, -1], [-1, 2], [0, 2]))
console.log(fourSumCount([0], [0], [0], [0]))