nums = [int(input()) for _ in range(9)]
total = sum(nums)
extra = total - 100

for i in range(9):
    for j in range(i+1, 9):
        if nums[i]+nums[j] == extra and nums[i] != nums[j]:
            for n in nums:
                if n != nums[i] and n != nums[j]:
                    print(n)
            exit(0)
