def digit_sum_replacement(A):
    """
    The input is an integer array, you can do
    1. Replace a number in the array by the sum of its digits
    2. A number can be selected multiple times
    3. At most two moves can be applied

    What is the minimun sum of array ?

        Example 1: 
         - Input: [1, 10, 12, 3]
         - Output: 8. Since we can turn input into [1, 1, 3, 3] by
         replacing 10 and 12 into 1 and 3

    """
    def digits_sum(num: int):
        return sum([int(n) for n in str(num)])

    losts = []

    for num in A:

        # Do first time
        ds1 = digits_sum(num)
        losts.append(num - ds1)

        # Do second time
        ds2 = digits_sum(ds1)
        losts.append(ds1 - ds2)

    # Get top two lost
    losts.sort(reverse=True)
    top_2_losts = losts[:2]

    return sum(A) - sum(top_2_losts)