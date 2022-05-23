def function(num):
    output = []
    for i in range(1, num+1):
        if((i % 3 != 0 and i % 5 != 0) or (i % 15 == 0)):
            output.append(i)
    return output

a = function(15)
print(a)