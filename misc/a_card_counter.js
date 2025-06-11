// На стол в ряд выложены карточки, на каждой карточке написано натуральное число.
// За один ход разрешается взять карточку либо с левого, либо с правого конца ряда. Всего можно сделать k ходов.
// Итоговый счет равен сумме чисел на выбранных карточках. Определите, какой максимальный счет можно получить по итогам игры.

// Формат ввода
// В первой строке записано число карточек n (1 ≤ n ≤ 105).
// Во второй строке записано число ходов k (1 ≤ k ≤ n).
// В третьей строке через пробел даны числа, записанные на карточках. i-е по счету число записано на i -й слева карточке.
// Все числа натуральные и не превосходят 10^4.

// Формат вывода
// Выведите единственное число —- максимальную сумму очков, которую можно набрать, сделав k ходов.

function getCardCount(n, k, cards) {
    let currentSum = cards.slice(0, k).reduce((acc, num) => acc + num, 0);
    let maxSum = currentSum;
    let left = k - 1;
    let right = n - 1;
    while (k > 0) {
        currentSum -= cards[left];
        currentSum += cards[right];
        if (currentSum > maxSum) {
            maxSum = currentSum;
        }
        k--;
        left--;
        right--;
    }
    return maxSum;
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
  const k = readInt();
  const cards = readArray();
  const ans = getCardCount(n, k, cards);
  console.log(ans);
}

function readInt() {
  const n = Number(_inputLines[_curLine]);
  _curLine++;
  return n;
}

function readArray() {
  const arr = _inputLines[_curLine]
    .trim()
    .split(" ")
    .map((num) => Number(num));
  _curLine++;
  return arr;
}
