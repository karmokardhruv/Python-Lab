m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix = []; columns = []
for i in range(0,m):
  matrix += [0]
for j in range (0,n):
  columns += [0]
for i in range (0,m):
  matrix[i] = columns
for i in range (0,m):
  for j in range (0,n):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix[i][j] = int(input())
print (matrix)


n=int(input("enter number of elements: ") )
list1=[]
for i in range(n) :
    a=input( )
    list1. append(a)
print("list is: ", list1)
