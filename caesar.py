def partial_sums(*nums):
    sum = 0
    sums = [0]
    for i in nums:
        sum += i
        sums.append(sum)
    return sums


print(partial_sums(1, 0.5, 0.25, 0.125))