function rob(nums) {
  if (nums === null || nums.length === 0) {
    return 0;
  } else if (nums.length == 1) {
    return nums[0];
  }

  let runningTotal = [];
  runningTotal[0] = nums[0];
  runningTotal[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    runningTotal[i] = Math.max(
      nums[i] + runningTotal[i - 2],
      runningTotal[i - 1]
    );
  }

  return runningTotal[runningTotal.length - 1];
}

// https://leetcode.com/problems/house-robber/
