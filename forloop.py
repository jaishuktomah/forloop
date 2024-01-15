# fruits = ["apple", "banana", "orange"]
# for x in fruits:
#     print(x)

# for x in "namraj":
#     print(x)

# dict_data = {
#     "name":"namraj",
#     "age":20
# }
# for x in dict_data:
#     print(dict_data[x])
    
# fruits = ["apple", "banana", "orange"]
# fruits.append("apple")    
# for items in fruits:
#     # print(items)
#     if items == "orangs":
#         # continue
#         break
#     print(items)


# dict_data = {
#     "a":1,
#     "b":2,
#     "c":1.1
# }  
# for x in dict_data:
#     if isinstance(dict_data[x],float):
#         break
#     print(dict_data[x])
    
# data = [1,2,3,4.4,5,6] 
# for x in data:
#     if isinstance(x,float):
#         break
#     print(x)
# a = input("enter a number")


# display multiplication table
# a = int(input("enter a number"))
# for i in range(1, 11):
#     print(f'{a} X {i} = {a*i}')
    

# a = [2,4,5,9]  
# for x in a:
#     print("\n")
#     for i in  range(1, 11):
#         print(f'{x} x {i} = {x*i}')

user_data = int(input("enter number"))

if user_data<5:
       for a in range(1,user_data+1,1):
           multi_data = int(input("enter a number==>"))
           for i in range(1,11,1):
               print(f'{multi_data} x {i} = {multi_data*i}')


else:   
    print("number should not greatwr than 5") 
  



        
        
    



    
 