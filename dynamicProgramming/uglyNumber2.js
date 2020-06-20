function uglyNumber(n) {
    let dp = [1];
    let i2 = 0;
    let i3 = 0;
    let i5 = 0;

    while (dp.length < n) {
        let m2 = dp[i2] * 2;
        let m3 = dp[i3] * 3;
        let m5 = dp[i5] * 5;
        let newAnswer = Math.min(m2, m3, m5);
        if (newAnswer == m2) {
            i2++;
        } if (newAnswer == m3) {
            i3++;
        }
        if (newAnswer == m5) {
            i5++;
        }
        dp.push(newAnswer);
    }
    return dp[n-1];
}