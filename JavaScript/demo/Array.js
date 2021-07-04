// const arr = Array(5).fill(0) // [ 0, 0, 0, 0, 0 ]
// const arr = [...Array(5)].map(x => 0) // [ 0, 0, 0, 0, 0 ]
// const arr = Array(5).fill(null).map((_, i) => i); // [ 0, 1, 2, 3, 4 ]
// const arr = Array.from({length: 5}, (v, i) => i) // [ 0, 1, 2, 3, 4 ]

// let temp = 0
// for (let i=0; i<arr.length; i++) {
//   arr[i] = temp
//   temp ++;
// }

// console.log(arr)

// const arr = Array(5).fill([])
// const arr = [...Array(5)].map(x => []) 
// const arr = Array.from({ length: 5 }, _ => [])

let temp = 0
for (let i=0; i<arr.length; i++) {
  arr[i].push(temp)
  temp ++;
}

console.log(arr)

const arr = Array(5).fill('')
// const arr = [...Array(5)].map(x => []) 
// const arr = Array.from({ length: 5 }, _ => '')

let temp = 0
for (let i=0; i<arr.length; i++) {
  arr[i] += temp.toString()
  temp++;
}

console.log(arr)