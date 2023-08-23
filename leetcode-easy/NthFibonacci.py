def getNthFib(n):
    # with recursion: O(n) time, extra space for recursive stack
    # if n == 1:
    #     return 0
    # elif n == 2:
    #     return 1
    # else:
    #     return getNthFib(n - 1) + getNthFib(n - 2)

    # with iteration: O(n) time, O(1) space
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev_but_one = 0
        prev = 1
        
        res = 1
        for i in range(3, n+1):
            res = prev + prev_but_one
            prev_but_one = prev
            prev = res 
        return res
        
        
        
