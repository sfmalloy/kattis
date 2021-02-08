N = gets.to_i
for i in 1..N
  line = gets.split().map(&:to_i)
  k = line[0]
  o = line[1..]
  s = 0
  o.each do |outlet|
    s += outlet - 1
  end
  puts s + 1
end