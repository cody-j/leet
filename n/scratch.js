const rand = (inclusiveMax) => {
    return Math.floor(Math.random() * (inclusiveMax + 1));
}

const arr = []
let i = 0;

while (i < 20) {
    arr.push(rand(40));
    i++
}

const two_sum = (arr, sum) => {
    arr.sort((a,b)=>a-b);
    console.log(arr)
    let i = 0;
    let j = arr.length-1

    while (i<j) {
        const s = arr[i] + arr[j];
        if (s === sum) return [arr[i],arr[j]]
        if (s < sum) {
            i += 1
        } else {
            j -= 1
        }
    }
    return -1
}

const words = ['worm', 'cat', 'bat', 'tab', 'dog', 'god', 'bare', 'bear', 'night', 'thing', 'two']

const anagrams = (words) => {
    const o = words.reduce((results, word) => {
        const hash = word.split('').sort().join('');
        if (results[hash]) {
            results[hash].push(word)
        } else {
            results[hash]=[word]
        }
        return results
    }, {})
    return Object.values(o)
}

const mat = [
    [1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0],
]

function contiguousCells(matrix) {
    const seen = new Set();
    const horizon = [];
    let largestBlock = 0;
    
    for (let n = 0; n < 5; n+=1) {
        for (let m = 0; m < 5; m+=1) {
            if (matrix[n][m] === 1) {
                console.log(n, m)
            }
        }
    }

}

contiguousCells(mat)
