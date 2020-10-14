function maxSubarray(nums) {
  let subSum = 0;
  let largestSum = -Infinity;

  for (let i = 0; i < nums.length; i++) {
    for (let j = i; j < nums.length; j++) {
      subSum += nums[j];
      if (largestSum < subSum) {
        largestSum = subSum;
      }
    }
  }
  return largestSum;
}

function maxSubarray2(nums) {
  let maxCurrent = nums[0];
  let maxGlobal = nums[0];

  for (let i = 0; i < nums.length; i++) {
    maxCurrent = Math.max(maxCurrent + nums[i], nums[i]);
    if (maxGlobal < maxCurrent) {
      maxGlobal = maxCurrent;
    }
  }

  return maxGlobal;
}
