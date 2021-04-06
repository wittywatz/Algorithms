function RomanNumeralReduction(str) {
  const numerals = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  const numerals2 = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
  };
  let out_str = '';
  const num_list = [1000, 500, 100, 50, 10, 5, 1];
  const str_length = str.length;
  let number = 0;
  for (let i = 0; i < str_length; i++) {
    number += numerals[str[i]];
  }

  let j = 0;
  while (number > 0) {
    const num_to_subtract = num_list[j];
    if (num_to_subtract > number) {
      j++;
    } else {
      number -= num_to_subtract;
      out_str += numerals2[num_to_subtract];
    }
  }

  // code goes here
  return out_str;
}

// keep this function call here
console.log(RomanNumeralReduction(readline()));
