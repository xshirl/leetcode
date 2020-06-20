function minTotal(triangle) {
  const len = triangle.length;
  if (!triangle || !len) {
    return 0;
  }
  const minArr = triangle[len - 1];
  for (let i = len - 2; i >= 0; i--) {
    for (let j = 0; j <= i; j++) {
      minArr[j] = Math.min(minArr[j], minArr[j + 1]) + triangle[i][j];
    }
  }
  return minArr[0];
}
