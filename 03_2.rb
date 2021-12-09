oxygen=""
carbon=""
data = readlines.map(&:chomp)
tempData = data.map(&:chomp)
data0 = []
data1 = []
oi = 0
while true do
    tempData.each_with_index do |line, y|
        if line.chars[oi] == "1"
            data1.push(line)
        end
        if line.chars[oi] == "0"
            data0.push(line)
        end
    end
    oi += 1
    if data0.length > data1.length
        tempData = data0
    else
        tempData = data1
    end
    if tempData.length == 1
        oxygen = tempData[0]
        break
    end
    data0 = []
    data1 = []
end
oi = 0
tempData = data.map(&:chomp)
while true do
    tempData.each_with_index do |line, y|
        if line.chars[oi] == "1"
            data1.push(line)
        end
        if line.chars[oi] == "0"
            data0.push(line)
        end
    end
    oi += 1
    if data0.length <= data1.length
        tempData = data0
    else
        tempData = data1
    end
    if tempData.length == 1
        carbon = tempData[0]
        break
    end
    data0 = []
    data1 = []
end
puts oxygen.to_i(2) * carbon.to_i(2)