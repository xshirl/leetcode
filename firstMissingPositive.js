var firstMissingPositive = function (nums) {
  let compareNums = [];
  nums.sort(function (a, b) {
    return a - b;
  });

  for (let i = 1; i <= nums.length + 1; i++) {
    compareNums.push(i);
  }

  for (let i = 0; i < compareNums.length; i++) {
    if (nums.indexOf(compareNums[i]) == -1) {
      return compareNums[i];
    }
  }

  if (nums.length == 0) {
    return 1;
  }
};

// https://leetcode.com/problems/first-missing-positive/
