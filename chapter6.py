# -*- coding: utf-8 -*-
# 第6章：字典 — 键值对，比列表更聪明

# ==========================================
# 6.1 字典是什么：花括号 {}，里面是 键:值
# ==========================================

# 列表用位置找人：person[0] 是啥？得记住顺序
# 字典用名字找人：person["name"] → 直接拿到

person = {"name": "小明", "age": 18, "city": "北京"}

print(person["name"])      # 小明
print(person["age"])       # 18
print(person["city"])      # 北京

# ==========================================
# 6.2 增删改查
# ==========================================

dog = {"name": "旺财", "age": 3}

# 查
print(dog["name"])           # 旺财

# 改
dog["age"] = 4               # 把年龄改成4
print(dog)                   # {'name': '旺财', 'age': 4}

# 增（直接写新键就行）
dog["color"] = "黄色"        # 没有 color 这个键？自动加上
print(dog)                   # {'name': '旺财', 'age': 4, 'color': '黄色'}

# 删
del dog["age"]
print(dog)                   # {'name': '旺财', 'color': '黄色'}

# get() 查 — 键不存在不会报错，返回默认值
print(dog.get("age", "没有年龄"))     # 没有age → 没有年龄
print(dog.get("name", "没有名字"))    # 有name → 旺财

# ==========================================
# 6.3 遍历字典
# ==========================================

user = {"name": "小红", "age": 22, "city": "上海"}

# 遍历键值对
for key, value in user.items():
    print(f"{key}→  {value}")
# name → 小红
# age → 22
# city → 上海

# 只遍历键
for key in user.keys():
    print(key)                    # name, age, city

# keys() 可以省略，for key in user 效果一样
for key in user:
    print(key)

# 只遍历值
for value in user.values():
    print(value)                  # 小红, 22, 上海

# ==========================================
# 6.4 字典嵌套（字典里放列表、字典里放字典）
# ==========================================

# 字典里放列表
student = {
    "name": "小刚",
    "scores": [85, 90, 78, 92]     # 成绩是列表
}
print(student["scores"][0])        # 第1个成绩 → 85
print(sum(student["scores"]))      # 总分 → 345

# 字典列表（列表里每个元素是字典）
students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78},
]

for s in students:
    print(f"{s['name']} 考了 {s['score']} 分")
# 小明 考了 85 分
# 小红 考了 92 分
# 小刚 考了 78 分

# ==========================================
# 🎯 你的练习
# ==========================================

# 练习1：创建一个字典存你自己的信息（名字、年龄、城市），打印所有键值对
my = {"name": "郝天才","age": 24,"city":"上海" }
for key,value in my.items():
    print(f"{key}--> {value}")

# 练习2：创建一个字典存3种食物和它的价格，让用户输入食物名，
#        用 get() 查价格，查不到就打印"没有这个"
foods ={"苹果":4,"西瓜":5,"桃子":6}
food=input("输入水果名")
price=(foods.get(food,"没有这个"))
if price=="没有这个":
    print(price)
else:
    print(f"{price}元")


# 练习3：创建一个字典列表存3个手机信息（品牌、型号、价格），
#        遍历打印每个手机的完整信息
phones = [
    {"品牌":"华为","型号":"mate80","价格":6000},
    {"品牌":"小米","型号":"17u","价格":5000},
    {"品牌":"1加","型号":"18u","价格":4000},

]

for p in phones:
    print(f"{p['品牌']},{p['型号']},{p['价格']}")


