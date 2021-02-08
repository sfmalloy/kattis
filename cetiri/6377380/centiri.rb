nums = gets.split.map(&:to_i).sort

diff = []
for i in 0..1
  d = nums[i+1] - nums[i]
  diff.push(d)
end

pattern = diff.min
new_nums = []
curr = nums[0]
found = false
for i in 0..2
  curr += pattern
  if !nums.include? curr
    found = true
    p curr
    break
  end
end

if not found
  p nums[0]
end