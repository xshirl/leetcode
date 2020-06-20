var lengthOfLastWord = function (s) {
  if (s == "") {
    return 0;
  }

  s = s.trim();
  arr = s.split(" ");
  return arr[arr.length - 1].length;
};
