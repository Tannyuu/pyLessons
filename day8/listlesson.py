import pprint
data = list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
pprint.pprint(data)

W=10
H=10
data=[None]*H
for i in range(H):
    data[i]=[0]*W
pprint.pprint(data)

data=[[0]*W]*H
pprint.pprint(data)

data[1][1]=5
pprint.pprint(data)

data=[[0]*W for i in range(H)]
pprint.pprint(data)
