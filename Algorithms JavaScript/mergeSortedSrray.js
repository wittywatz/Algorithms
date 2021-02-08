//Given two sorted arrays, merge them in sorted order.

arr1 = [1, 3, 6, 25];
arr2 = [2, 4, 6, 30];

const mergeSortedArrays = (array1, array2) => {
  const mergedArray = [];
  let i = 0;
  let j = 0;
  if (array1.length == 0) {
    return array2;
  }
  if (array2.length == 0) {
    return array1;
  }

  while (array1 || array2) {
    if (!array1[i] && !array2[j]) {
      return mergedArray;
    }
    if (!array1[i]) {
      const remaining = array2.slice(j);
      console.log('Array1 is undefined', remaining);
      return [...mergedArray, ...remaining];
    }
    if (!array2[j]) {
      const remaining = array1.slice(i);
      console.log('Array2 is empty', remaining);
      return [...mergedArray, ...remaining];
    }
    if (array1[i] <= array2[j]) {
      mergedArray.push(array1[i]);
      i++;
    } else {
      mergedArray.push(array2[j]);
      j++;
    }
  }
  return mergedArray;
};
console.log(
  mergeSortedArrays([1, 3, 6, 25, 30, 30, 31, 35, 38, 40], [2, 4, 30, 30])
);
