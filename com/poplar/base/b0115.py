# coding=utf-8
score = 77
if score > 90:
    print 'perfect'
    print 'You are the winner!'
elif score > 80:
    print 'Good'
    print 'You should try your best!'
elif score > 60:
    print 'Just soso'
else:
    print '!!!!!!!!!!!!!!!!!!!!!!'


# for in形式循环
# names = ['aaa', 'bbb', 'ccc']
names = ('aaa', 'bbb', 'ccc')
for name in names:
    print 'Hello: ', name

sum = 0;
for i in range(101):
    sum += i;
print sum

arr = (123,)
print (10)
print len((10,))
print arr
print len(arr)
print range(10)

birth = raw_input('you birth year: ')
#将字符串转成int类型数据
print birth < 2000
print int(birth) < 2000

