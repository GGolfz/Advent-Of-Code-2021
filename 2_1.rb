x=0
y=0
readlines.map(&:to_s).each do |data|
    direction, distance = data.split(' ')
    distance = distance.to_i
    case direction
        when 'up'
            y += distance
        when 'forward'
            x = x + distance
        when 'backward'
            x -= distance
        when 'down'
            y -= distance
    end
end
puts (x*y).abs