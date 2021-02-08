nums = list(map(int, input().split()))
def is_sorted():
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
      return False
  return True

def swap(a, b):
  t = nums[a]
  nums[a] = nums[b]
  nums[b] = t

while not is_sorted():
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
      swap(i, i + 1)
      [print(k, end=' ') for k in nums]
      print()