/**
 * @param {number[]} digits
 * @return {number[]}
 */
 var plusOne = function(digits) {
    let res = digits;
    for (let i=digits.length-1; i>=0; i--) {
        let current = digits[i];
        if (current === 9) {
            res[i] = 0;
            if (i === 0) {
                res.unshift(1);
            }
        } else {
            res[i] = current + 1
            break
        }
    }
    return res;
};

console.log(plusOne([1,2,3]))
console.log(plusOne([4,3,2,1]))
console.log(plusOne([0]))
console.log(plusOne([9]))