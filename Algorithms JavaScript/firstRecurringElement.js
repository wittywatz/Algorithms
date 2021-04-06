//Code goes here
const firstRecurringElement = (arr) => {
  let seen = {};
  for (let i = 0; i < arr.length; i++) {
    if (seen[arr[i]]) {
      return arr[i];
    }
    seen[arr[i]] = true;
  }
  return null;
};

const result = firstRecurringElement([1, 2, 3, 4, 1]);
console.log(result);
