list = [1, 2, 3, 4, 5]
newList = [list[0]]
for i in range(len(list)):
    newList.append(list[i] + list[i - 1])
    # print(i)
   
print(newList)