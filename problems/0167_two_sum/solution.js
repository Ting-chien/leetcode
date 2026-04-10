/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(numbers, target) {
    let res = []
    let remains = {}
    for (let i=0; i<numbers.length; i++) {
        const remain = target - numbers[i]
        if (Object.keys(remains).includes(remain.toString())) {
            res = [remains[remain], i+1]
        } else {
            remains[numbers[i]] = i+1
        }
    }
    return res;
};

console.log(twoSum([2,7,11,15], 9))
console.log(twoSum([2,3,4], 6))
console.log(twoSum([-1,0], -1))