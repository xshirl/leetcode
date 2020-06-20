var searchMatrix = function (matrix, target) {
  for (const row of matrix) {
    if (row.length != 0 && row[0] <= target && row[row.length - 1] >= target) {
      if (binarySearch(row, target)) return true;
    }
  }

  return false;
};

var binarySearch = function (row, target) {
  if (row.length == 0) return false;
  mid = Math.floor((row.length - 1) / 2);

  if (row[mid] > target) {
    return binarySearch(row.slice(0, mid), target);
  }
  if (row[mid] < target) {
    return binarySearch(row.slice(mid + 1, row.length), target);
  }
  return true;
};
