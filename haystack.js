function findNeedle(haystack, needle) {
  for (let i = 0; i < haystack.length; i++) {
    for (let j = i + 1; j < haystack.length; j++) {
      if (haystack.slice(i, j) == needle) {
        return i;
      }
    }
  }
  return -1;
}

console.log(findNeedle("hello", "ll"));

function findNeedle2(haystack, needle) {
  let index = -1;
  for (let i = 0; i < haystack.length; i++) {
    if (haystack.substring(i, i + needle.length) == needle) {
      return i;
    }
  }
  return index;
}

console.log(findNeedle2("hello", "ll"));

// https://leetcode.com/problems/implement-strstr/submissions/
