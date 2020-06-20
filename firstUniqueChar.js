function firstUniqueChar(s) {
  let arr = s.split("");
  let hashMap = {};

  for (let char of arr) {
    hashMap[char] ? hashMap[char]++ : (hashMap[char] = 1);
  }

  for (let i = 0; i < arr.length; i++) {
    if (map[arr[i]] == 1) {
      return i;
    }
  }
  return -1;
}

// https://leetcode.com/problems/first-unique-character-in-a-string/
