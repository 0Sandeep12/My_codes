list_1 = [6,7,2,3,3,5,1,9,8,8,8,8]
dict_1 = {}
list_1.sort()
max_1 = max(list_1)
for i in range(1,max_1+1):
    dict_1[i] = 0
for elem in list_1:
    dict_1[int(elem)] +=1
for key, elem in dict_1.items():
    if(elem > 1):
        print("duplicate: "+str(key))
    if(elem == 0):
        print("missing: "+str(key))
