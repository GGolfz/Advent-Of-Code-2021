prev=-1
count=0
readlines.map(&:to_i).each do |n|
    if prev == -1
        prev = n
    elsif n > prev
        count += 1
    end
    prev = n
end
puts count