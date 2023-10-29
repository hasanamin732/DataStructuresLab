import numpy as np

def create_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    x=np.empty((rows,cols))
    for i in range(rows):
        for j in range(cols):
            coord=float(input(f"Enter the value for row {i+1} and column {j+1} "))
            x[i][j]=coord
    return x

def transpose(x):
    rows=x.shape[0]
    cols=x.shape[1]
    result=np.empty((cols,rows))
    for i in range(rows):
        for j in range(cols):
            result[j][i]=x[i][j]
    return result


def diagnol(x):
    rows=x.shape[0]
    cols=x.shape[1]
    result=np.empty((rows,cols))
    for i in range(rows):
        for j in range(cols):
            if i==j:
                result[i][j]=1
            elif j>i:
                result[i][j]=0
            else:
                result[i][j]=2
    return result

x=np.empty((5,5))
my_mat=create_matrix()
print(my_mat)
print()
print(f"Transposed Matrix:\n {transpose(my_mat)}")
print()
print(f"Diagnol Matrix:\n {diagnol(x)}")





