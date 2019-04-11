num_list = ['7','5','3','1','9']
target = 12
num_list.sort()
print(num_list)

j = len(num_list) - 1
i = 0
for elem in num_list:
    if(int(num_list[i]) + int(num_list[j]) == target):
        print(str(i)+','+str(j))
        i = i+1
    elif(int(num_list[i]) + int(num_list[j]) > target):
        j = j-1
    else:
        i = i+1
