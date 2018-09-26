# 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 访问列表中的元素
print(bicycles[0])
# 首字母大写
print(bicycles[0].title())
# 访问1和3处的自行车
print(bicycles[0])
print(bicycles[2])
# 切片
print(bicycles[2:3:])
# 列表中的各个值
message = "My first bicycles was a " + bicycles[0].title()
print(message)
# 修改，添加，删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
# 根据索引修改
motorcycles[0] = 'ducati'
print(motorcycles)
# 在列表末尾添加元素
motorcycles.append('DaYang')
print(motorcycles)
# 在列表中插入元素
'''第一位'''
motorcycles.insert(0, 'DUkadi')
'''第三位'''
motorcycles.insert(3, 'DUkadi')
print(motorcycles)
# 从列表中删除元素
'''使用del语句'''
del motorcycles[0]
del motorcycles[2]
del motorcycles[3]
print(motorcycles)
'''使用pop()。pop尾部删除，可以访问被删除的值'''
popped_motocycles = motorcycles.pop()
print(motorcycles)
print(popped_motocycles)
new_motorcycles = ['honda', 'yamaha', 'suzuki']
last_motocycles = new_motorcycles.pop()
print("The last motocycle I owned was a " + last_motocycles.title() + '.')
# 根据值删除元素
new_motorcycles.remove('honda')
print(new_motorcycles)
# range
b = []
for i in range(10):
    if i not in b:
        b.append(i)
print(b)
# 练习
"""
1,创建列表aList中的元素，移除每个元素的空格，增加一个元素’python’,
2,并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
3,并添加到一个新列表中,最后循环打印这个新列表，用两种方法删除一个元素，转化为元组。
"""
# 1
aList = ['taibai ', 'alexC', 'AbC ', 'egon', ' Ritian', ' Wusir', ' aqc']
dList = []
for i in aList:
    dList.append(i.strip())
print(aList)
print(dList)
dList.insert(0, 'python')
# 2-3
bList = []
for i in dList:
    if i.startswith('a') or i.startswith('A') and i.endswith('c'):
        bList.append(i)
print(bList)
# 循环打印列表
for i in bList:
    print(i)
bList.pop()
print(bList)
"""
开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
敏感词列表 li = ["苍老师","东京热",”薄熙来”]，则将用户输入的内容中的敏感词汇替换成***，
并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
"""
li = ["苍老师", "东京热", "薄熙来"]
a = input("请输入词汇：")
b = []
for i in li:
    if a == i:
        a.replace(a, '***')
        print("您的输入包含敏感词汇！")
    else:
        b.append(a)

"""
创建一个包含1-100之间所有素数的列表，排序后打印显示该列表；随后只保留该列表前5个数字，
删除其余内容并打印输出相应结果；再将每个元素值加上100，显示列表内容；把列表转化为字符串。
"""
eList = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        eList.append(i)
print(eList)
# 保留前五
new_eList = eList[0:5:1]
print(new_eList)
# 每个元素加上100
new_eLists = []
for i in new_eList:
    i = i + 100
    new_eLists.append(i)
print(new_eLists)
# 转为字符串
strs = [str(i) for i in new_eLists]
s = ''.join(strs)
print(s)
"""
用合适的数据结构实现以下几个案例
n	9*9乘法表
n	100以内的素数
n	1—20的数字的阶乘
"""
# 9*9乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(i, j, i * j), end='')
    print()
# 100以内的素数（质数）
cList = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        cList.append(i)
print(cList)

# 1-20的数字阶乘
'''递归实现'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


sums = factorial(20)
print(sums)
