def hourglassSum(arr):
  """
  Given 2D array should have minimum size of 3x3
  """
  maxSum = float('-inf')
  n = len(arr)-2
  for i in range(n):
    for j in range(n):
      hourglassTop = sum(arr[i][j:j+3])
      hourglassMiddle = arr[i+1][j+1]
      hourglassBottom = sum(arr[i+2][j:j+3])
      hourGlassSum = hourglassTop+hourglassMiddle+hourglassBottom
      maxSum = max(maxSum,hourGlassSum)
  return maxSum