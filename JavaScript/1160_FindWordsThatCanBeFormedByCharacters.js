/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
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

// 參考方法1
// var countCharacters = function(words, chars) {
//   chars = chars.split('').sort().join('')
//   function canFormed(str){
//       str = str.split('').sort().join('');
//       let j = 0;
//       for(let i = 0; i < chars.length; i++){
//           if(chars[i] === str[j]) j++;
//           if(j === str.length) return true;
//       }
//       return false;
//   }
  
//   let res = 0;
//   for(let word of words){
//   if(word.length > chars.length) continue;
//       if(canFormed(word)) res += word.length
//   }
//   console.log(res);
// };


countCharacters(["cat", "bt", "hat", "tree"], "atach")
countCharacters(["hello", "world", "leetcode"], "welldonehoneyr")
countCharacters(["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin", "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh", "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx", "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop", "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx", "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr", "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo", "oxgaskztzroxuntiwlfyufddl", "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp", "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv", "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz", "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue", "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv", "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob", "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs", "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
  , "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp")