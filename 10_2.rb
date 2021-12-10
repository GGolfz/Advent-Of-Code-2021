scores = []
readlines.map(&:to_s).map { | line |
    arr = []
    score = 0
    chk = true
    line.split('').each { |char|
        if char == '(' or char == '[' or char == '{' or char == '<'
            arr.push(char)
        else
            if arr.length == 0
                puts "error"
            else
                if char == ')' and arr.pop != '('
                    chk = false
                    break
                elsif char == ']' and arr.pop != '['
                    chk = false
                    break
                elsif char == '}' and arr.pop != '{'
                    chk = false
                    break
                elsif char == '>' and arr.pop != '<'
                    chk = false
                    break
                end
            end
        end
    }
    if chk and arr.length > 0
        while arr.length > 0  do
            char = arr.pop()
            if char == '('
                score *= 5
                score += 1
            elsif char == '['
                score *= 5
                score += 2
            elsif char == '{'
                score *= 5
                score += 3
            elsif char == '<'
                score *= 5
                score += 4
            end
        end
        scores << score
    end
}
def median(array)
    return nil if array.empty?
    sorted = array.sort
    len = sorted.length
    return (sorted[(len - 1) / 2] + sorted[len / 2]) / 2
end
puts median(scores)