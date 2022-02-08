for i in range(151):
    print(i)

for i in range(5,1001,5):
    print(i)

for count in range(1,101):
    if(count%10==0):
        print("CodingDojo", count)
    elif(count%5==0):
        print("Coding", count)
    else:
        print(count)

def odd_sum():
    sum = 0
    for i in range(1,500001,2):
        sum = sum+i
    return sum
print(odd_sum())

for j in range(2018,0,-4):
    print(j)

lowNum = 2
highNum = 9
mult = 3
for k in range(lowNum, highNum +1):
    if(k%mult==0):
        print(k)