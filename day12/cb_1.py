from math import pow

print(pow(10,2))

def funcA(z):
    ans = z * 2
    print(ans)

def funcB(x,y):
    z = x + y
    funcA(z)

x = 10
y = 20
funcB(10,20)

print('Hello')

my_list = [10,20,30]

x = 10

if(x < 10) :
    print('hoge')
else:
    print('foo')

print('こんにちは')

print('hello' + str(x))

print('hello'*5)

def hello(x,y):
    print(x + ',' + y)
hello('Hello','Python')

def hello(x):
    print('Hello,'+ x)
hello('World')

if x >= 100:
    print('hoge')
else:
    print('foo')

if x >=100:
        print('hoge')
        print('foo')

my_list = [10,20,30]
my_list[2]

my_dict = {'hoge':1,'foo':2}
print(my_dict['foo'])

x = '100'
x = int(x)

a=100

def hoge():
    global a
    print(a)
    a=10
hoge()
print(a)#10

x = 0
while x < 10:
    print('Hello')
    x +=1

try:
    price = int(input('料金を入力>>'))
    number = int(input('人数を入力>>'))
    print('1人あたり{}円です'.format(price / number))
except ValueError:
    print('料金または人数は整数を入力してください')
except ZeroDivisionError:
    print('人数に0は入力しないでください')
else:
    print('正常終了')
finally:
    print('ok')
print('プログラムを終了します')
