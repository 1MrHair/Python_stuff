a_list = ['This','is','a','list',1,2,3,4,5]
for i in range(len(a_list)):
    print(a_list[i])
a_list[9:12] = 6,7,8
print(a_list)
print(a_list[-1])
print(len(a_list))
a_list.pop(11)
print(len(a_list))
a_list2 = ['2nd','list']
a_list3 = a_list + a_list2
print(a_list3)
