import sys
check_list = []
input_str = "[{()}]"
open_list = "[{("
close_list = "]})"
#print(len(input_str))
for i in range(0,len(input_str)):
    ind1 = -1
    ind = -2
    #print(input_str[i])
    if(input_str[0] == ']'):
        print("unbalanced")
        sys.exit()
    check_list.append(input_str[i])
    check_len = len(check_list)
    if(check_len > 1):
        if(check_list[check_len-1] in close_list):
            ind = close_list.index(check_list[check_len-1])
        if(check_list[check_len-2] in open_list):
             ind1 = open_list.index(check_list[check_len-2])
        if(ind == ind1):
            check_list.pop(check_len-1)
            check_list.pop(check_len-2)
if(len(check_list) == 0):
    print("balanced")
else:
    print("unbalanced")
