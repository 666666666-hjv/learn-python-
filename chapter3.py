# -*- coding: utf-8 -*-
# 第3章：列表 — 把一堆东西放在一起

# ==========================================
# 3.1 列表是什么
# ==========================================

# 方括号 [] 包起来，逗号分隔
fruits = ["apple", "banana", "orange", "grape"]
print(fruits)                # 输出整个列表

# 用位置（索引）取单个元素，从 0 开始数！
print(fruits[0])             # 第1个 → apple
print(fruits[1])             # 第2个 → banana
print(fruits[-1])            # -1 取最后一个 → grape
print(fruits[-2])            # -2 取倒数第二个 → orange

# 改元素
fruits[0] = "watermelon"     # 把第1个换成西瓜
print(fruits)

# ==========================================
# 3.2 增删改查
# ==========================================

numbers = [10, 20, 30]

# 加
numbers.append(40)           # 加到末尾
print(numbers)               # [10, 20, 30, 40]

numbers.insert(1, 15)        # 插到位置1
print(numbers)               # [10, 15, 20, 30, 40]

# 删
del numbers[0]               # 删位置0 → 10 没了
print(numbers)               # [15, 20, 30, 40]

popped = numbers.pop()       # 弹出最后一个 → 40
print(popped)                # 40
print(numbers)               # [15, 20, 30]

numbers.remove(20)           # 删掉值为 20 的那个
print(numbers)               # [15, 30]

# ==========================================
# 3.3 遍历列表（for 循环）— 最常用！
# ==========================================

names = ["小明", "小红", "小刚"]

for name in names:           # 逐个取出，每次叫 name
    print(f"你好，{name}!")
# 输出：
# 你好，小明！
# 你好，小红！
# 你好，小刚！

# 缩进很重要！缩进里的才算循环体
for name in names:
    print(f"{name} 在写代码")     # 这行在循环里
    print(f"{name} 很棒")         # 这行也在循环里
print("循环结束了")                # 这行不在循环里（没缩进）

# ==========================================
# 3.4 数字列表
# ==========================================

# range() 生成一串数字
for num in range(1, 6):      # 1到5（不含6）
    print(num)

# range() 转成列表
digits = list(range(1, 11))  # 1到10
print(digits)

# 简单的数字操作
print(min(digits))           # 最小值 → 1
print(max(digits))           # 最大值 → 10
print(sum(digits))           # 总和 → 55

# 列表推导式（快速生成列表）
squares = [x**2 for x in range(1, 6)]
print(squares)               # [1, 4, 9, 16, 25]

# ==========================================
# 3.5 切片（取列表的一部分）
# ==========================================

colors = ["红", "橙", "黄", "绿", "蓝", "紫"]

print(colors[0:3])           # 0到2 → ['红', '橙', '黄']
print(colors[:2])            # 开头到1 → ['红', '橙']
print(colors[3:])            # 3到末尾 → ['绿', '蓝', '紫']
print(colors[-3:])           # 倒数3个 → ['绿', '蓝', '紫']

# ==========================================
# 🎯 你的练习
# ==========================================

# 练习1：创建一个列表，放5个你喜欢的食物，然后打印第2个
fruits = ["苹果","西瓜","菠萝","芒果","梨"]
print(fruits[1])

# 练习2：用 for 循环遍历上面的列表，每条打印"我喜欢吃xxx"
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 练习3：用 range() 生成 1 到 100 的所有奇数，打印它们的数量
odds=list(range(1,101,2))
print(odds)
print(len(odds))
