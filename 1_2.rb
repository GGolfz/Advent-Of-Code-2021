prev=[]
count=0
readlines.map(&:to_i).each do |n|
    if prev.size >= 3
        if n + prev[-1] + prev[-2] > prev[-1] + prev[-2] + prev[-3]
            count += 1
        end
    end
    prev << n
end
puts count