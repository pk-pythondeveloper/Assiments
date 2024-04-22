
from array import*
#arrange in asscending order
# def asscending_order(arr,len):
#     for i in range(len):
#         for j in range(i+1,len):
#             if arr[i]>arr[j]:
#                 temp=arr[j]
#                 arr[j]=arr[i]
#                 arr[i]=temp
#     print(arr)
# arr=[12,11,45,23,17]
# len=len(arr)
# asscending_order(arr,len)

#descendin order
# def desscending_order(arr,len):
#     for i in range(len):
#         for j in range(i+1,len):
#             if arr[i]<arr[j]:
#                 temp=arr[j]
#                 arr[j]=arr[i]
#                 arr[i]=temp
#     print(arr)
# arr=[12,11,45,23,17]
# len=len(arr)
# desscending_order(arr,len)

# 2. Find the largest number in a given List without using the inbuilt method?
# def find_largest(arr,len):
#     max=arr[0]
#     for i in range(1,len):
#         if arr[i]>max:
#             max=arr[i]
#     print(max)
# arr = [20, 25,111, 10, 45, 22, 50, 40]
# len=len(arr)
# find_largest(arr,len)


# 3. Write a program for single inheritance in python?
#this is an example of  songle inhertance
# class parent:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         print(a+b)
# class child(parent):
#     def multi(self,a,b):
#         self.a=a
#         self.b=b
#         print(a+b)
# obj=child()
# obj.add(12,15)


# 4. Write a program for overloading and overriding.
#this is an example if method overrinding
# class parent:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         print(a+b)
#     def multi(self,a,b):
#         self.a=a
#         self.b=b
#         print(a+b)
# class child(parent):
#     def add(self,a,b,c):
#         self.a=a
#         self.b=b
#         print(a+b)
#     def multi(self,a,b,c):
#         self.a=a
#         self.b=b
#         print(a+b)
# obj=child()
# obj.add(12,15)

#this is an example of method overloding this finction is able to take multiple arrguments
# def add(*args):
#     result=0
#     for num in args:
#         result +=num
#     print('sum these number is',result)
#
# add(23,45,12)


# 5. Write a program for multiprocessing thread.
# import threading
# def print_cube(num):
#     print("Cube: {}".format(num * num * num))
# def print_square(num):
#     print("Square: {}".format(num * num))
# if __name__ == "__main__":
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
#     print("Done!")

# 6.wrinte a programs to add two matrices

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3,2,1]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)