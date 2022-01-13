import pprint
W=10
H=10

#data=[[0]*W for i in range(H)]
#pprint.pprint(data)


data=list()
for i in range(H):
    temp=list()
    for j in range(W):
        temp.append(0)
        data.append(temp)
pprint.pprint(data)

# ２重ループ
for i in range(H):
    temp=[None] * W
    for j in range(W):
        temp[j]=i*10+j+1
    data[i]=temp

pprint.pprint(data)

# 内包表記
data=[[i*10 + j for j in range(1,11)] for i in range(0,10)]
pprint.pprint(data)

x=[n for n in range(1,8)]
print(x)
#[1,2,3,4,5,6,7]

x=[n**2 for n in range(1,8)]
print(x)
#[1,4,9,16,25,36,49]

x=[n for n in range(1,8) if n % 2 ==0]
print(x)
#[2,4,6]

x=[n for n in range(2,7,2)]
print(x)
#[2,4,6]


x=[i*10+j for j in range(2,5) for i in range(1,3)]
print(x)
#[12,13,14,22,23,24]

x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)
#[[17,18,19],[27,28,29]]

row=col=3
matrix=[[1 if i == j else 0 for j in range(col)] for i in range(row)]
print(matrix)
[[1,0,0],[0,1,0],[0,0,1]]
