import random
print('数あてゲームを始めます。3桁の数を当ててください')
answer=[random.randint(0,9) for i in range(3)]

while True:
    prediction=[ int(input(f'{i}桁目の予想を入力(0~9)>>')) 
    for i in range(1,4)]
    hit=ball=0
    for i in range(len(prediction)):
        if prediction[i]==answer[i]:
            hit+=1
        else:
            for j in range(len(answer)):
                if i!=j and prediction[i]==answer[j]:
                    ball+=1
                    break;
    if hit== len(answer):
        print('正解です!')
        break
    print(f'{hit}ヒット!,{ball}ボール!')

    if int(input('続けますか?1:続ける2:終了>>')) !=1:
        print(answer)
        break
