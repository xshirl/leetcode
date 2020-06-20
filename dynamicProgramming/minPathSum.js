function minPathSum(grid) {
  var height = grid.length;
  var width = grid[0].length;

  for (var i = 0; i < height; i++) {
    for (var j = 0; j < width; j++) {
      if (i !== 0 && j !== 0)
        grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
      else if (i !== 0) grid[i][j] += grid[i - 1][j];
      else if (j !== 0) grid[i][j] += grid[i][j - 1];
    }
  }
  return grid[height - 1][width - 1];
}
