li=[]
li.append(int(input('国語>>')))
li.append(int(input('算数>>')))
li.append(int(input('理科>>')))
li.append(int(input('社会>>')))
li.append(int(input('英語>>')))

"""
let li=[];
li.push(10);
li.push(20);
let sum=0;
for(let i=0;i<li.length;i++){
    sum+=li[i];
}
console.log(`合計点${sum},平均点${sum/li.length}`)
"""
print(f'合計点{sum(li)},平均点{sum(li)/len(li)}')
