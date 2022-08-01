len, code, guess = gets.split
len = len.to_i - 1

r = 0
left_guess = []
left_code = {}
for i in 0..len do
    if code[i] == guess[i]
        r += 1
    else
        left_guess << guess[i]
        if left_code[code[i]] == nil
            left_code[code[i]] = 1
        else
            left_code[code[i]] += 1
        end
    end
end

s = 0
for i in 0..left_guess.length do
    if left_code[left_guess[i]] != nil and left_code[left_guess[i]] > 0
        s += 1
        left_code[left_guess[i]] -= 1
    end
end

puts "#{r} #{s}"
