function TrappingWater(arr) {
  let left = 0;
  let right = arr.length - 1;
  let total = 0;
  let leftMax = 0;
  let rightMax = 0;
  while (left < right) {
    if (arr[left] < arr[right]) {
      if (arr[left] >= leftMax) {
        leftMax = arr[left];
      } else {
        total += leftMax - arr[left];
      }
      left++;
    } else {
      if (arr[right] >= rightMax) {
        rightMax = arr[right];
      } else {
        total += rightMax - arr[right];
      }
      right--;
    }
  }
  // code goes here
  return total;
}

// keep this function call here
console.log(TrappingWater(readline()));
