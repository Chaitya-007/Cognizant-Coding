

input1 = 4
input2 = 5
l = [1,3,5,8]
cnt = 0

for i in range(input1):
    for j in range(i,input1):
        if l[i] + l[j] <= input2:
            print(l[i]," + ",l[j]," <= ",input2)
            cnt = cnt + 1


print("cnt = ",cnt)