const mergeSort = (arr) => {
  if (arr.length === 1) {
    return;
  }
  const low = 0;
  const high = arr.length - 1;
  const middle = parseInt((high + low) / 2);
  let left = arr.slice(0, middle + 1);
  let right = arr.slice(middle + 1);
  mergeSort(left);
  mergeSort(right);
  merge(arr, left, right);
};

const merge = (arr, left, right) => {
  let i = 0;
  let j = 0;
  let k = 0;
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      arr[k] = left[i];
      i++;
      k++;
    } else {
      arr[k] = right[j];
      j++;
      k++;
    }
  }

  while (i < left.length) {
    arr[k] = left[i];
    i++;
    k++;
  }
  while (j < right.length) {
    arr[k] = right[j];
    j++;
    k++;
  }
};
let arr = ['a', 'b', 'z', 'c', 'd'];
mergeSort(arr);

// const swap = (arr, index1, index2) => {
//   const temp = arr[index1];
//   arr[index1] = arr[index2];
//   arr[index2] = temp;
//   return arr;
// };

// console.log(swap(arr, 0, 3));
console.log(arr);
