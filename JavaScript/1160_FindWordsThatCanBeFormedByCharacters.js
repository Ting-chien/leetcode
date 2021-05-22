/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 * 
 * ### Naive Solution ###
 * Runtime: 256 ms
 * Memory: 47.1 MB
 */
var countCharacters = function (words, chars) {
  // 將 chars 整理成 object
  let charsObject = {}
  for (let char of chars) {
    if (Object.keys(charsObject).includes(char)) {
      charsObject[char] += 1;
    } else {
      charsObject[char] = 1;
    }
  }
  let res = [];
  // 將每個字串中的符號與 charsObject 的內容去做比對
  for (let word of words) {
    res.push(word);
    let currCharsObject = { ...charsObject }
    for (let char of word) {
      if (Object.keys(currCharsObject).includes(char)) {
        if (currCharsObject[char] > 0) {
          currCharsObject[char] -= 1;
        } else {
          res.pop();
          break;
        }
      } else {
        res.pop();
        break;
      }
    }
  }
  let length = res.reduce((prev, curr) => {
    return prev + curr.length
  }, 0)
  return length;
};

/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 * 
 * Sort and Two Pointers
 */
var countCharacters = function(words, chars) {
  // 先將chars按字母順序排列
  chars = chars.split('').sort().join('')

  // 建立比對字符是否夠用的函數
  function canFormed(str){
    str = str.split('').sort().join('');
    let j = 0;
    for(let i = 0; i < chars.length; i++){
      if(chars[i] === str[j]) j++;
      if(j === str.length) return true;
    }
    return false;
  }
  
  let res = 0;
  for(let word of words){
    // 如果字串長度大於chars就直接跳過
    if(word.length > chars.length) continue;
    // 接著再去比對words中的字串是否符合canFormed條件
    if(canFormed(word)) res += word.length;
  }
  
  return res;
};

/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 * 
 * Solution supported by Wesely
 * Runtime: 92 ms
 * Memory: 45 MB
 */
var countCharacters = function (words, chars) {
  let ans = 0;
  let available = Array(26).fill(0);
  for (let i=0; i<chars.length; i++) {
    // 將字符a-z轉成ascii code，參考 http://sticksandstones.kstrom.com/appen.html
    let index = chars.charCodeAt(i) - 97;
    available[index] += 1;
  }
  words.forEach(word => {
    // 將每個字串所用的字符也轉換成Array(26)的表示陣列
    let seen = Array(26).fill(0);
    for (let i=0; i<word.length; i++) {
      let index = word.charCodeAt(i) - 97;
      seen[index] += 1;
    }

    let valid = true;
    // 比較陣列availabel和seen中每個符號是否都夠用
    for (let i=0; i<26; i++) {
      if (seen[i] > available[i]) {
        valid = false;
        break;
      }
    }
    // 如果都夠，則將字串長度加到ans中
    if (valid) {
      ans += word.length;
    }
  })
  return ans;
}

console.log(countCharacters(["cat", "bt", "hat", "tree"], "atach"))
console.log(countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))