#!/usr/bin/node

function findSecondBiggest(args) {
  let max = -Infinity, result = -Infinity;

  for (const value of args) {
    const nr = Number(value);
    if (nr > max) {
      [result, max] = [max, nr];
    } else if (nr < max && nr > result) {
      result = nr;
    }
  }

  return result;
}

const numbers = process.argv.slice(2);

if (numbers.length < 2) {
  console.log(0);
} else {
  console.log(findSecondBiggest(numbers));
}
