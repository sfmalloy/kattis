from itertools import permutations

original = input()
nums = [int(''.join(p)) for p in permutations(list(map(str, original)))]

original = int(original)
mx = 0
for n in nums:
    if n > original and (n - original < mx - original or mx == 0):
        mx = n
print(mx)

