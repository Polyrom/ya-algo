// Вам дан массив натуральных чисел ai. Найдите число таких пар элементов (ai , aj) , где | ai − aj | % 200 == 0 и i < j.

// Формат ввода
// В первой строке дан размер массива n (1 ≤ n ≤ 200_000).
// Во второй строке через пробел записаны элементы массива ai (1 ≤ ai ≤ 109).

// Формат вывода
// Выведите единственное число — количество пар, подходящих под указанное выше условие.

const httpStatusOK = 200;

// Time: O(n), Memory = O(1)
// Key insights:
// 1. |a_i - a_j| % 200 == 0 is equivalent to a_i % 200 == a_j % 200
// 2. Store remainders in a frequency map to optimize space complexity (array in this case)
// 3. For each remainder rem that appears n times, the number of valid pairs is (freq[rem] * freq[rem] - 1) / 2 ("rem choose n", combination formula)
function getNumberOfGoodPairs(n, numbers) {
  let freq = Array(httpStatusOK).fill(0);
  let totalPairs = 0;
  for (let i = 0; i < n; i++) {
    const rem = numbers[i] % httpStatusOK;
    freq[rem] += 1;
  }
  for (let i = 0; i < freq.length; i++) {
    if (freq[i] >= 2) {
      totalPairs += (freq[i] * (freq[i] - 1)) / 2;
    }
  }
  return totalPairs;
}

const _readline = require("readline");

const _reader = _readline.createInterface({
  input: process.stdin,
});

const _inputLines = [];
let _curLine = 0;

_reader.on("line", (line) => {
  _inputLines.push(line);
});

process.stdin.on("end", solve);

function solve() {
  const n = readInt();
  const numbers = readArray();
  const ans = getNumberOfGoodPairs(n, numbers);
  console.log(ans);
}

function readInt() {
  const n = Number(_inputLines[_curLine]);
  _curLine++;
  return n;
}

function readArray() {
  var arr = _inputLines[_curLine]
    .trim(" ")
    .split(" ")
    .map((num) => Number(num));
  _curLine++;
  return arr;
}
