describe("plusOne", () => {
  it("is function and is defined ", () => {
    expect(plusOne).toBeDefined();
    expect(typeof plusOne).toBe("function");
  });

  it("return plus One to parametter", () => {
    expect(plusOne([9, 9, 9])).toEqual([1, 0, 0, 0]);
  });
});
