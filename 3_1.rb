arr=[0,0,0,0,0,0,0,0,0,0,0,0]
count=0
readlines.each do |line|
    line.split("").each_with_index do |c,i|
        arr[i]+=1 if c=="1"
    end
    count+=1
end
gamma=""
epsilon=""
arr.each do |i|
    if i > count/2
        gamma+="1"
        epsilon+="0"
    else
        gamma+="0"
        epsilon+="1"
    end
end
puts gamma.to_i(2) * epsilon.to_i(2)