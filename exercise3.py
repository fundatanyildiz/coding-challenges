def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # for a 1-step staircase n is 1
    # for a 2-step staircase n is 2
    steps = [1, 2]
    # for reach the top you should take n steps
    # you can either climb 1 or 2 steps
    # how many distinct ways can you climb to the top
    for i in range(2, n):
        a = steps[i - 1] + steps[i - 2]
        steps.insert(i, a)
    return steps[n - 1]

