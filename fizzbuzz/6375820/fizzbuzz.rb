x, y, n = gets.split().map(&:to_i)
for i in 1..n
  b = ((i % x == 0 ? "Fizz" : "") + (i % y == 0 ? "Buzz" : ""))
  puts b == "" ? i : b
end