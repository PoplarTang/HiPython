def func(a, b, c=0, *args, **kwargs):
    print 'a=', a, 'b=',b, 'c=',c, 'args=', args, 'kw=', kwargs

print func(1,2)
print func(1,2,3)
print func(1,2,3, 'x','y', name='aaa')