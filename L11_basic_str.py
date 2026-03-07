s = "Eason Chan"

# get
# 正向索引：从0开始
print(s[3])
# 反向索引：从-1开始
print(s[-7])

# update：str不可变，不允许修改

# for
for i in s:
	print(i, end = "\t")
else:
	print()

# 切片 s[start(默认0):end(默认-1):step(默认1)]
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])
print(s[6:10:1])
print(s[6::1])
print(s[6::])
print(s[::2])

# reverse
print(s[-1:-11:-1])

# 常用方法
# length
print(len(s))
# in return bool
print('Eason' in s)
# find():查找指定字符串第一次出现的索引位置
sf = s.find("Chan")
print(sf)
# count():统计子字符串在字符串中出现的次数
count = s.count('a')
print(count)
# upper():小写转大写
su = s.upper()
print(su)
# lower():大写转小写
sl = s.lower()
print(sl)
# split():字符串切割
split = s.split(' ')
print(split)
# strip():去除前后空格或指定字符串
st = s.strip()
print(st)
# replace():将字符串中的指定字符串进行替换
ns = s.replace("a", "A")
print(ns)
# startswith()、endswith():判断字符串是否以指定字符串开头或结尾，return bool
print(s.startswith("Eason"))
print(s.endswith("chan"))
print(f"观察字符串操作后，原字符串的变化: {s} --> 无变化！")