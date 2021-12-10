score = 0
readlines.map(&:to_s).map { | line |
    arr = []
    line.split('').each { |char|
        if char == '(' or char == '[' or char == '{' or char == '<'
            arr.push(char)
        else
            if arr.length == 0
                puts "error"
            else
                if char == ')' and arr.pop != '('
                    score += 3
                    break
                elsif char == ']' and arr.pop != '['
                    score += 57
                    break
                elsif char == '}' and arr.pop != '{'
                    score += 1197
                    break
                elsif char == '>' and arr.pop != '<'
                    score += 25137
                    break
                end
            end
        end
    }
}
puts score