# coding=utf-8
names=['Job','Favourite','Thinking']
print len(names)
print names[-1] #打印倒数第一个
names.append('Append')
print names[-1]
names.pop()
print names
names.insert(0, 'First')
print names[0]


t = ('aaa', 'bbb', ['xx', 'yy'])
t[2][0] = 'X'

# t[0] = '111' # TypeError: 'tuple' object does not support item assignment
print t

