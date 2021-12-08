count = 0
readlines.map do |line|
    line.split(" | ")[1].split(" ").map(&:to_s).each do |element| 
        size = element.size
        if size == 2 or size == 3 or size == 4 or size == 7
            count+=1
        end
    end
end
puts count