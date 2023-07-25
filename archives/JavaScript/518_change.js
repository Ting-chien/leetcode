function rec(n, coins) {
    if(n === 0) { // 0 組合
        return 1
    }

    //	n  != 0
    if(coins.length === 0) { // 沒coin
        return 0
    }
    if(coins.length === 1) { // 最後一個
        return n % coins[0] === 0 ? 1 : 0  // ex: n = 4, coins[0] = 2
    }

    let sum = 0;
    const tailCoin = coins[coins.length - 1];
    const otherCoins = coins.slice(0, coins.length - 1);
    for(let i = 0; i * tailCoin <= n; i++) {
        console.log("Using " + i + " " + tailCoin + " coin(s)")
        const subCombineList = rec(n - i * tailCoin, otherCoins);
        sum += subCombineList;
    }
    return sum;
}

/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
var change = function(amount, coins) {
    coins.sort((a, b) => a - b);
    const newCoins =  coins.filter(coin => coin <= amount);

    const result = rec(amount, newCoins);
    return  result;
};

console.log(change(500, [1,2,5]))