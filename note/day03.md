## 字符串和编码

* 如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
* 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

* 把字母和对应的数字相互转换：

``` python
>>> ord('A')
65
>>> chr(65)
'A'
```

* unicode表示字符串

~~~phyton
u'中'
u'\u4e2d'	4e2d是16进制的Unicode码

print u'中文'
中文
~~~

* unicode字符串->utf-8 编码

~~~phyton
>>> u'ABC'.encode('utf-8')
'ABC'

>>> u'中文'.encode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'
~~~

* utf-8编码字符串->Unicode字符串

~~~phyton
>>> 'abc'.decode('utf-8')
u'abc'

>>> '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
u'\u4e2d\u6587'

>>> print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
中文
~~~

* 源代码包含中文时, 在文件开头声明编码, 因为文件内容是以Unicode进行编码存储的

~~~phyton
#!/usr/bin/env python
# -*- coding: utf-8 -*-
~~~

> - 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
> - 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码























