# range(start,end)=>range(1,4)=>its for loop 4time
# for index in range(1,5):
#     print(index)#1 to 4
 
# # when start is not present 
# for index in range(5):
#     print(index) #0 to 4
# how to print list elements in new line
list=[1,6,3,4,12,15]
# print(list[1])
# print(len(list))

# for index in list:
#     print(index)

for index in range(len(list)):
    print(index,"index")
    print(list[index],"element")
    if list[index]==6:
     print(list[index]) 