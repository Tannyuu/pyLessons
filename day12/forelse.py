import random

data=[random.randint(0,9) for i in range(10)]
#randintはrandrangeでもok
print(data)
if 7 in data:
    print(f'index{data.index(7)}に７はありました')
else:
    print('7はありませんでした')




'''
number = list()
for n in range(10):
    number.append(randint(0,10))

else:
    print('7はありませんでした')
'''


'''
for i in range(10):
    if i==7:
        break
    print(i)
else:
   print('完了')
'''
