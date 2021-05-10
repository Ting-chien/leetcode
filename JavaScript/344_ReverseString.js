/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
  // Method1. Naive
  // for (let i=0; i<=s.length; i++) {
  //   let temp = s.pop();
  //   s.splice(i, 0, temp);
  // }

  // Method2. Half-loop
  for (let i=0; i<s.length/2; i++) {
    [s[i], s[s.length-i-1]] = [s[s.length-i-1], s[i]];
  }
  console.log(s);
};

reverseString(["h","e","l","l","o"])
reverseString(["H","a","n","n","a","h"])