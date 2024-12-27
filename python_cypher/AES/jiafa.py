import math
import time 



# my_list = 10,20,30,49
# a,b,*c=my_list
# print(my_list)
# print('a=',a,'b=',b,'c=',c)
# print(type(c),type(my_list))


# m = 'nihaowojiaozhangzishua'
# if len(m)%2 != 0:
#     m+='i'
# print(m)
start_time = time.time()


result = ""


for i in range(10000):


    result += "test"


end_time = time.time()


print(f"加号操作符耗时: {end_time - start_time}秒")


