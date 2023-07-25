/**
 * @param {string[]} strs
 * @return {string[][]}
 * 
 * key: 遍歷，O(n)
 * runtime: 132 ms
 * memory: 50 MB
 */
var groupAnagrams = function(strs) {
  const hash = {};

  function sort(str) {
    return str.split('').sort().join('');
  }

  for (let i=0; i<strs.length; i++) {
    const str = strs[i];
    const key = sort(str);
    if (!hash[key]) {
      hash[key] = [str];
    } else {
      hash[key].push(str);
    }
  }

  return Object.values(hash);
};

/**
 * @param {string[]} strs
 * @return {string[][]}
 * 
 * key: 桶排序，O(n * k) n 为数组长度，k 为字符串的平均长度.
 * runtime: 148 ms
 * memory: 50.4 MB	
 */
var groupAnagrams = function(strs) {
  const hash = {};

  // 利用桶排序，建立26字母的陣列並將每個字母出現的次數記錄在counts
  for (let i=0; i<strs.length; i++) {
    let str = strs[i];
    let counts = Array(26).fill(0);
    for (let j=0; j<str.length; j++) {
      counts[str.charCodeAt(j) - 97]++;
    }
    // 將counts轉換成key可接受的值
    const key = counts.join("-");
    if (!hash[key]) {
      hash[key] = [str];
    } else {
      hash[key].push(str);
    }
  }

  return Object.values(hash);
};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
console.log(groupAnagrams([""]))
console.log(groupAnagrams(["a"]))