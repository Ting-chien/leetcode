// /**
//  * @param {number[]} nums
//  * @param {number} k
//  * @return {number[]}
//  */
// var topKFrequent = function(nums, k) {
//   let counts = {};
//   for (let num of nums) {
//     if (!counts[num]) {
//       counts[num] = 1;
//     } else {
//       counts[num] ++;
//     }
//   }
//   let orders = Array(nums.length+1).fill([]);
//   for (let entry of Object.entries(counts)) {
//     orders[entry[1]] = orders[entry[1]].concat([parseInt(entry[0])])
//   }
//   return orders.flat().slice(-k);
// };

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 * 
 * 備註：參考助教寫法後改寫，改寫部分包括
 * 1. 將 object 改成 Map，讓key不用去做String<->Number之間的轉換
 * 2. 使用Array.from()讓buckets中陣列的處理不會因為記憶體位址而彼此影響
 */
var topKFrequent = function(nums, k) {
  const counts = new Map();
  const buckets = Array.from({ length: nums.length + 1 }, _ => [])
  for (const num of nums) {
    counts.set(num, (counts.get(num) || 0) + 1)
  }
  for (const entry of counts.entries()) {
    const [n, freq] = entry;
    buckets[freq].push(n);
  }
  return buckets.flat().slice(-k);
};

console.log(topKFrequent([1,1,1,2,2,3], 2))
console.log(topKFrequent([1], 1))
console.log(topKFrequent([-1, -1], 1))