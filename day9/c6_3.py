userinfo = input('名前と血液型をカンマで区切って1行で入力>>')
[name,blood] = userinfo.split(',')
blood = blood.upper().split()
print('{}さんは{}型なので大吉です'.format(name,blood))
