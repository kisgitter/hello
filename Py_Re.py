#介绍python正则表达式模块使用
import re

#match从字符串起始位置开始匹配，只有在字符串位置0匹配成功才有返回
re.match(r'\d\d\d','123456789')

#search扫描整个字符串匹配并返回第一个匹配结果
re.search(r'\d\d\d','123456789')

#split用于分割字符串，返回list
re.split(r'\s+','are you ok')

#sub用于替换字符串，语法为sub( 要替换的字符 ,替换为字符 , 原始字符串 ),返回替换后字符串
re.sub(r'\d\d\d','abc','123a456b789')

#subn类似sub，只是返回值为一个tuple，内容为替换后字符串和替换次数
re.subn(r'\d\d\d','abc','123a456b789')

#预编译正则表达式，作用是 1、正则表达式可以重用 2、大量使用正则表达式时预编译能提高效率
reg = re.compile(r'\d\d\d')
reg.findall('123456789')

#正则表达式分组，用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m.group(0) #'010-12345' 整体匹配结果
m.group(1) #'010' 第一个分组
m.group(2) #'12345'第二个分组
m.groups() #('010','12345') 子串的集合

#写一个邮箱的正则表达
re_email = re.compile(r'[A-Za-z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')



