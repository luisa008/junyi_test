'''Input is a num
output is a string'''

def throw(num):
    output = []
    for i in range(1, num+1):
        if((i % 3 != 0 and i % 5 != 0) or (i % 15 == 0)):
            output.append(i)
    return output

def test():
    a = 15
    a_t = [1, 2, 4, 7, 8, 11, 13, 14, 15]
    if(throw(a) == a_t): return True

# unit test
print(test())

# input
# num = int(input())
# print(throw(num))