count1=[1,2,3,4,5,6,7,8,9,]
count2=[1,2,3,4,5,6,7,8,9,]
ans=0
for num1 in range(len(count1)):
    for num2 in range(len(count2)):       
        ans=count1[num1]*count2[num2]
        print(ans)
