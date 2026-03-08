list = [33, 22, 44, 55, 66, 77, 88, 55, 22 ,"100", True]
print(type(list))
print(len(list))

# get
# 正向索引：从0开始
print(list[0])
# 反向索引：从-1开始
print(list[-11])

# update
list[10] = 111
print(list)

# delete
del list[10]
print(list)

# for
for i in list:
	print(i, end= "\t")
else:
	print()

# 常见方法
# append(): 在列表尾部追加元素
list.append(888)
print(f"【append()】 list:{list}")
# insert(): 在指定索引之前插入元素_eg:insert(index_num, item)
list.insert(-1, 666)
print(f"【insert()】 list:{list}")
# remove(): 移除列表中第一个匹配到的元素
list.remove("100")
print(f"【remove()】 list:{list}")
# pop(): 删除列表中指定索引位置的元素(默认最后一个)
p1 = list.pop()
print(f"【pop()】 p1:{p1}; list:{list}")
p2 = list.pop(1)
print(f"【pop(1)】 p2:{p2}; list:{list}")
# sort(): 对列表进行排序(注意：需要列表元素的数据类型一致才可排序)
list.sort()
print(f"【sort()】 list:{list}")
# reverse(): 反转列表元素
list.reverse()
print(f"【reverse()】 list:{list}")


# 合并列表
print()
print("====== 合并列表 ======")
num_list1 = [11, 2, 23, 442, 445, 55, 21]
num_list2 = [45, 2, 14, 26, 85, 36, 111]
num_list = [*num_list1, *num_list2]
print(f"【合并1-解包&组包】 num_list = [num_list1*，num_list2*] ===> {num_list}")
num_list = num_list1 + num_list2
print(f"【合并2-+】 num_list = num_list1 + num_list2 ===> {num_list}")
# 去重(这里用到not in)
new_list = []
for item in num_list:
	if item not in new_list:
		new_list.append(item)
print(new_list)

# 推导式(案例)
# 格式1：列表名称 = [要插入列表的数据 for i in 列表]
# 格式2：列表名称 = [要插入列表的数据 for i in 列表 if 条件]
print()
print("====== 推导式 ======")
pre_list = range(1, 31)
after_list = [i for i in pre_list if i % 3 == 0 or i % 5 == 0]
print(after_list)