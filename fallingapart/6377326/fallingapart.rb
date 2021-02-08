n = gets.to_i
nums = gets.split.map(&:to_i).sort.reverse()
a = 0
b = 0

for i in 0..n-1
  if i % 2 == 0
    a += nums[i]
  else
    b += nums[i]
  end
end

puts "#{a} #{b}"