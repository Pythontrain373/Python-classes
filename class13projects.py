row=int(input("Enter the numbeer of rows: "))
for i in range(1,row+1):
        print(" "*(row-i),end=" ")
        print("*"*i)