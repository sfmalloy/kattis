require "readline"

x, y, n = gets.split().map(&:to_i)
for i in 1..n
  if i % x == 0 && i % y == 0
    puts "FizzBuzz"
  elsif i % x == 0
    puts "Fizz"
  elsif i % y == 0
    puts "Buzz"
  else
    puts i
  end
end