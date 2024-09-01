def fizzbuzz(nums):
    start = nums[0]

    while start <= (nums_length := len(nums)):
        if start % 3 == 0 and start % 5 == 0:
            print("FizzBuzz")
            start += 1
            continue
        elif start % 3 == 0:
            print("Fizz")
            start += 1
            continue
        elif start % 5 == 0:
            print("Buzz")
            start += 1
            continue
        else:
            print(start)
            start += 1
            continue


nums = list(range(1, 31))
fizzbuzz(nums)
