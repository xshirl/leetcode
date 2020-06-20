let isPalindrome = function (x) {
  if (x < 0) {
    return false;
  }

  return x == reverse(x);

  function reverse(num) {
    let reversed = 0;
    while (num > 0) {
      reversed = reversed * 10 + (num % 10);
      num = Math.floor(num / 10);
    }
    return reversed;
  }
};

console.log(isPalindrome(121));

// https://leetcode.com/problems/palindrome-number/
