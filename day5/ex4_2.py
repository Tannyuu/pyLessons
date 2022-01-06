count = 0
print('カレーを召し上がれ')
while True:
    print(f'{count}皿のカレーを食べました')
    okawari = input('おかわりはいかがですか?(y/n)')
    if okawari == 'y':
        count+=1
        continue
    elif okawari =='n':
        print('ごちそうさまでした')
        break

