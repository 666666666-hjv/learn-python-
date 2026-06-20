# -*- coding: utf-8 -*-
# ============================================================
# 第1-7章 复习总纲 — 你掌握的所有兵器
# ============================================================

print("=" * 50)
print("第2章：变量、字符串、数字")
print("=" * 50)

# --- 变量：给数据起名字 ---
name = "郝天才"          # 字符串用引号
age = 24                 # 数字不用引号
score = 95.5             # 小数（浮点数）

# --- 字符串操作 ---
print(name.title())      # 首字母大写
print(name.upper())      # 全大写
print(name.lower())      # 全小写

# --- f-string：花括号里放变量 ---
print(f"我叫{name}，今年{age}岁")

# --- 数字运算 ---
print(age + 5)           # 加法
print(age - 3)           # 减法
print(age * 2)           # 乘法
print(age / 2)           # 除法
print(age ** 2)          # 乘方

# --- 类型转换 ---
print("我今年" + str(age) + "岁")     # str() 数字→字符串
number = int("123")                   # int() 字符串→数字

print()

# ============================================================
print("=" * 50)
print("第3章：列表")
print("=" * 50)

fruits = ["苹果", "西瓜", "菠萝", "芒果", "梨"]

# --- 索引（从0开始！）---
print(fruits[0])         # 第1个 → 苹果
print(fruits[1])         # 第2个 → 西瓜
print(fruits[-1])        # 最后1个 → 梨
print(fruits[-2])        # 倒数第2个 → 芒果

# --- 增删改 ---
fruits.append("香蕉")    # 加末尾
fruits.insert(0, "草莓") # 插到位置0
print(fruits)

del fruits[0]            # 删位置0
popped = fruits.pop()    # 弹最后，同时拿到被弹的
print(f"被弹掉的是：{popped}")
fruits.remove("苹果")    # 删值为"苹果"的

# --- for 循环 ---
for f in fruits:
    print(f"我喜欢吃{f}")

# --- range() ---
for i in range(1, 6):    # 1到5（不含6）
    print(i, end=" ")
print()

# --- 切片：取一段 ---
colors = ["红", "橙", "黄", "绿", "蓝", "紫"]
print(colors[:3])        # 前3个
print(colors[3:])        # 位置3到最后
print(colors[-2:])       # 最后2个

# --- 数字列表 ---
nums = list(range(1, 11))
print(f"总和：{sum(nums)}，最大：{max(nums)}，最小：{min(nums)}")

# --- len()：数长度 ---
print(f"列表里有{len(fruits)}个水果")

print()

# ============================================================
print("=" * 50)
print("第4章：切片循环、复制列表、元组")
print("=" * 50)

# --- 遍历切片 ---
names = ["小明", "小红", "小刚", "小美", "小强"]
for n in names[:3]:      # 只遍历前3个
    print(n, end=" ")
print()

# --- 复制列表（坑！）---
a = [1, 2, 3]
b = a[:]                 # ✅ 真复制，各管各的
c = a                    # ❌ 贴标签，改一个全改
b.append(999)
print(f"a = {a}")        # a 没变
print(f"b = {b}")        # b 多了 999

# --- 元组：不能改的列表 ---
point = (10, 20)         # 圆括号
print(point[0])          # 取值一样
# point[0] = 30          # ❌ 报错！元组不能改
point = (30, 40)         # ✅ 可以整个重写

print()

# ============================================================
print("=" * 50)
print("第5章：if 判断")
print("=" * 50)

# --- 比较符号 ---
x = 10
print(x == 10)           # True  等于
print(x != 5)            # True  不等于
print(x > 5)             # True  大于
print(x < 20)            # True  小于
print(x >= 10)           # True  大于等于

# --- 组合条件 ---
print(x > 5 and x < 20)  # True  两个都成立
print(x > 5 or x < 1)    # True  一个成立就行
print(not x > 100)       # True  取反

# --- in / not in ---
foods = ["汉堡", "披萨", "炸鸡"]
print("披萨" in foods)   # True
print("寿司" not in foods) # True

# --- if-elif-else ---
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")        # ← 走到这里
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 从上到下检查，命中就停

print()

# ============================================================
print("=" * 50)
print("第6章：字典")
print("=" * 50)

# --- 字典 = 键值对 ---
person = {"name": "小明", "age": 18, "city": "北京"}

print(person["name"])    # 按键取值 → 小明
person["job"] = "学生"   # 加新键值对
person["age"] = 19       # 改值
del person["city"]       # 删键值对

# --- get()：安全取值 ---
print(person.get("name", "无名"))       # 有 → 小明
print(person.get("score", "没有分数"))  # 没有 → 没有分数

# --- 遍历 ---
for key, value in person.items():
    print(f"{key} → {value}")

for key in person.keys():       # 只拿键
    print(key)

for value in person.values():   # 只拿值
    print(value)

# --- 字典嵌套 ---
students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78},
]
for s in students:
    print(f"{s['name']} 考了 {s['score']} 分")

print()

# ============================================================
print("=" * 50)
print("第7章：while 循环")
print("=" * 50)

# --- while：条件成立就一直跑 ---
count = 1
while count <= 3:
    print(count, end=" ")
    count = count + 1       # 一定要改条件，不然死循环！
print()

# --- break：立刻跳出 ---
i = 0
while True:
    i = i + 1
    if i == 5:
        break                # 跳到第5次，不跑了
    print(i, end=" ")
print("→ break退出了")

# --- continue：跳过本轮 ---
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue             # 跳过3
    print(i, end=" ")
print("→ 跳过了3")

# --- while 处理列表 ---
tasks = ["学Python", "写代码", "做项目"]
while tasks:
    task = tasks.pop()
    print(f"处理：{task}")

print()

# ============================================================
print("=" * 50)
print("综合练习：把前面学的都用上")
print("=" * 50)

# 练习1：创建一个字典存商品价格，用 while + input 做一个购物查询
#        输入商品名显示价格，输入 q 退出，查不到提示无此商品
print("\n--- 练习1：商品价格查询 ---")

# TODO: 你的代码


# 练习2：创建学生成绩列表（字典列表），遍历打印每个人的信息，
#        然后只打印分数 >= 80 的学生（if 过滤）
print("\n--- 练习2：学生成绩筛选 ---")

# TODO: 你的代码


# 练习3：创建一个列表放待办事项，用 while + pop 处理，
#        每处理一个都用 f-string 打印，最后打印共处理了多少个（用 len）
print("\n--- 练习3：待办处理报告 ---")

# TODO: 你的代码
