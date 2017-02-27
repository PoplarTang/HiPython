# coding=utf-8
# 定义字典
map = {'aaa':123, 'bbb':234,'ccc':345.6}

# 获取字典指定元素
print map['aaa']

print map

# 修改字典某个元素
map['bbb'] = 'hhh'

print map

# 判断字典是否包含某个元素
print 'bbb in map: ', 'bbb' in map
print 'fff in map: ', 'fff' in map

# 安全的获取字典中的元素
print map.get('ddd')
print map.get('ddd', -1)

# 删除字典元素
map.pop('bbb')

print map

# set集合， 不可放入list可变对象
s = {1, 2, 3, 4, 3}
print s
s.add(1) # 添加
s.add(5)
print s
s.remove(2) # 移除
print s
# 两个集合的操作
s2 = {'123', 234, 3}
s_all = s | s2
s_cross = s & s2
print s_all
print s_cross

s = {11,22, (1, 2, 3)}
print s

m = {(1, 2, 3): 123, (1, 2, (3, 4)): 234}
print m

tupleList = (3,4,[2,4]);
print tupleList
map = {'aaa':23, 'vvv':12, tupleList:333}
print map;



