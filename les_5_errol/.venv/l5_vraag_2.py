def prime_nums(nums):
    for num in nums:
        if num == 1:
            continue
        x = 2
        while num >= x:
            if num == x:
                print(num)
                break
            elif num % x == 0:
                break
            else:
                x+=1


nums = list(range(1, 100))
prime_nums(nums)