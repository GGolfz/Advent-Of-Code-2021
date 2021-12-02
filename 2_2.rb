x=0
y=0
aim=0
readlines.map(&:to_s).each do |data|
    direction, distance = data.split(' ')
    distance = distance.to_i
    case direction
        when 'up'
            aim -= distance
        when 'forward'
            x = x + distance
            y = y + aim*distance
        when 'down'
            aim += distance
    end
end
puts (x*y).abs