function maxArea(height) {
  let left = 0;
  let right = height.length - 1;
  let area = 0;

  while (left < right) {
    area = Math.max(area, (right - 1) * Math.min(height[left], height[right]));
    if (height[left] < height[right]) left++;
    else {
      right--;
    }
  }
  return area;
}

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
