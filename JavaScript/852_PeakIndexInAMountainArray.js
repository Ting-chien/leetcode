/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
  let prevNum = -1;
  for (let i=0; i<=arr.length; i++) {
    if (arr[i] > prevNum) {
      prevNum = arr[i];
    } else {
      return i-1;
    }
  }
};

console.log(peakIndexInMountainArray([0,1,0]))
console.log(peakIndexInMountainArray([0,2,1,0]))
console.log(peakIndexInMountainArray([0,10,5,2]))
console.log(peakIndexInMountainArray([3,4,5,1]))
console.log(peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))