//Given two sorted arrays, merge them in sorted order.
const mergeSortedArrays = (array1, array2) => {
  //Arrays must be Sorted
  const mergedArray = [];
  let i = 0;
  let j = 0;
  //Assumes that two arrays would be passed and must be sorted
  if (array1.length == 0) {
    return array2;
  }
  if (array2.length == 0) {
    return array1;
  }

  while (array1 || array2) {
//     if (!array1[i] && !array2[j]) {
//       return mergedArray;
//     }   //May never get to this line of code
    if (!array1[i]) {
      return [...mergedArray, ...array2.slice(j)];
    }
    if (!array2[j]) {
      return [...mergedArray, ...array1.slice(i)];
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
// console.log(
//   mergeSortedArrays([1, 3, 6, 25, 30, 30, 31, 35, 38, 40], [2, 4, 30, 30])
// );
