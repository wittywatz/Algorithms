// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let sum = 0;
  let len = A.length;
  for (let i = 0; i < len; i++) {
    if (Math.abs(A[i] % 4) === 0) {
      sum += A[i];
    }
  }
  return sum;
}

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S, C) {
  // write your code in JavaScript (Node.js 8.9.4)
  let temp_arr = S.split('\n');
  const len = temp_arr.length;
  let keys = temp_arr[0].split(',');
  let obj_len = keys.length;
  obj = {};
  for (let i = 0; i < obj_len; i++) {
    obj[keys[i]] = [];
  }
  for (let i = 1; i < len; i++) {
    let units = temp_arr[i].split(',');
    for (let i = 0; i < obj_len; i++) {
      obj[keys[i]].push(units[i]);
    }
  }
  const sum = Math.max.apply(null, obj[C]);
  return sum;
}

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, D) {
  // write your code in JavaScript (Node.js 8.9.4)
  let cardPaymentSum = {};
  let cardPayment = {};
  let n = 12;
  let sum = 0;
  len_D = D.length;
  for (let i = 0; i < len_D; i++) {
    let str = D[i][5] + D[i][6];
    if (A[i] < 0) {
      if (!(str in cardPayment)) {
        cardPaymentSum[str] = 0;
        cardPayment[str] = [];
      }
      cardPayment[str].push(A[i]);
      cardPaymentSum[str] += A[i];
    }
    sum += A[i];
  }

  for (let j in cardPayment) {
    if (cardPayment[j].length > 2 && Math.abs(cardPaymentSum[j]) > 99) {
      n -= 1;
    }
  }
  return sum - 5 * n;
}
