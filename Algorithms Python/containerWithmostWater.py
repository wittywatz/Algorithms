def maxArea(height):
  left = 0
  right = len(height)-1
  max_area = 0
  while left < right:
      min_height = min(height[left], height[right])
      width = right-left
      area = min_height * width
      max_area = max(max_area,area)
      if height[left] <= height[right]:
          left+=1
      else:
          right -=1
  return max_area