sum = 0
readlines.map do |line|
    sum_line = ""
    input, output = line.split(" | ")
    input = input.split(" ")
    arr = ["","","","","","",""]
    s2 = input.find {|x| x.size == 2}
    s3 = input.find {|x| x.size == 3}
    s4 = input.find {|x| x.size == 4}
    s7 = input.find {|x| x.size == 7}
    s5 = input.find_all {|x| x.size == 5}
    s5_1 = s5[0]
    s5_2 = s5[1]
    s5_3 = s5[2]
    s6 = input.find_all {|x| x.size == 6}
    s6_1 = s6[0]
    s6_2 = s6[1]
    s6_3 = s6[2]
    arr[0] = s3.split('') - s2.split('')
    if (s5_1.split('') - s2.split('')).size == 3
        if (s5_2.split('') - s4.split('')).size == 3
            arr[5] = (s5_1.split('') - s5_2.split(''))[0]
            arr[4] = (s5_2.split('') - s5_1.split(''))[0]
            arr[1] = (s5_3.split('') - s5_1.split(''))[0]
            arr[2] = (s2.split('') - s5_3.split(''))[0]
            s6_temp = s6.find {|x| x.size == 6 and (x.split('') - s5_3.split('')).size == 2}
            arr[3] = (s5_3.split('') - s6_temp.split(''))[0]
        elsif (s5_3.split('') - s4.split('')).size == 3
            arr[5] = (s5_1.split('') - s5_3.split(''))[0]
            arr[4] = (s5_3.split('') - s5_1.split(''))[0]
            arr[1] = (s5_2.split('') - s5_1.split(''))[0]
            arr[2] = (s2.split('') - s5_2.split(''))[0]
            s6_temp = s6.find {|x| x.size == 6 and (x.split('') - s5_2.split('')).size == 2}
            arr[3] = (s5_1.split('') - s6_temp.split(''))[0]
        end
    elsif (s5_2.split('') - s2.split('')).size == 3
        if (s5_1.split('') - s4.split('')).size == 3
            arr[5] = (s5_2.split('') - s5_1.split(''))[0]
            arr[4] = (s5_1.split('') - s5_2.split(''))[0]
            arr[1] = (s5_3.split('') - s5_2.split(''))[0]
            arr[2] = (s2.split('') - s5_3.split(''))[0]
            s6_temp = s6.find {|x| x.size == 6 and (x.split('') - s5_3.split('')).size == 2}
            arr[3] = (s5_3.split('') - s6_temp.split(''))[0]
        elsif (s5_3.split('') - s4.split('')).size == 3
            arr[5] = (s5_2.split('') - s5_3.split(''))[0]
            arr[4] = (s5_3.split('') - s5_2.split(''))[0]
            arr[1] = (s5_1.split('') - s5_2.split(''))[0]
            arr[2] = (s2.split('') - s5_1.split(''))[0]
            s6_temp = s6.find {|x| x.size == 6 and (x.split('') - s5_1.split('')).size == 2}
            arr[3] = (s5_1.split('') - s6_temp.split(''))[0]
        end
    elsif (s5_3.split('') - s2.split('')).size == 3
        if (s5_2.split('') - s4.split('')).size == 3
            arr[5] = (s5_3.split('') - s5_2.split(''))[0]
            arr[4] = (s5_2.split('') - s5_3.split(''))[0]
            arr[1] = (s5_1.split('') - s5_3.split(''))[0]
            arr[2] = (s2.split('') - s5_1.split(''))[0]
            s6_temp = s6.find {|x| x.size == 6 and (x.split('') - s5_1.split('')).size == 2}  
            arr[3] = (s5_1.split('') - s6_temp.split(''))[0]
        elsif (s5_1.split('') - s4.split('')).size == 3
            arr[5] = (s5_3.split('') - s5_1.split(''))[0]
            arr[4] = (s5_1.split('') - s5_3.split(''))[0]
            arr[1] = (s5_2.split('') - s5_3.split(''))[0]
            arr[2] = (s2.split('') - s5_2.split(''))[0]
            s6_temp = s6.find {|x| x.size == 6 and (x.split('') - s5_2.split('')).size == 2}
            arr[3] = (s5_2.split('') - s6_temp.split(''))[0]
        end
    end
    ["a","b","c","d","e","f","g"].each do |x|
        if not arr.include? x
            arr[6] = x
        end
    end
    output.split(" ").map(&:to_s).each do |element| 
        size = element.size
        if size == 2
            sum_line += "1"
        elsif size == 3
            sum_line += "7"
        elsif size == 4
            sum_line += "4"
        elsif size == 5
            if element.include? arr[2] and element.include? arr[4]
                sum_line += "2"
            elsif element.include? arr[2] and element.include? arr[5]
                sum_line += "3"
            elsif element.include? arr[1] and element.include? arr[5]
                sum_line += "5"
            end
        elsif size == 6
            if element.include? arr[2] and element.include? arr[4]
                sum_line += "0"
            elsif element.include? arr[4] and element.include? arr[5]
                sum_line += "6"
            elsif element.include? arr[2] and element.include? arr[3]
                sum_line += "9"
            end
        elsif size == 7
            sum_line += "8"
        end
    end
    sum += sum_line.to_i
end
puts sum