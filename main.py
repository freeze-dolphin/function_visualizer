import utils
import turtle as tt

print("如果计算出错画出来的是红线")
print("通常情况下只有在值不存在时会出现红线")
print("正常应该是默认的黑线", end="\n\n")
print("以下为一些用法说明", end="\n\n")
print("使用 <> 代替开平方")
print(" · 例如: <2> 表示 √2", end="\n\n")
print("幂运算使用 ^ 号")
print("或使用 Python 内建的 ** 运算符")
print(" · 例如: 2 ^ 4 等价于 2 ** 4", end="\n\n")
print("默认导入了 math 模块")
print("使用 Python 语法可以使用模块内的所有函数")
print("或者使用 `#函数名()` 的格式来直接引用模块内的函数")
print(" · 例如: math.pow(5, 3) 表示 5 的 3 次方")
print(" · 例如: #ceil(1.1) 会被解释为 2 且等价于 math.ceil(1.1)", end="\n\n")
print("同样导入了 random 模块")
print("与 math 模块同理但格式为 `$函数名()`", end="\n\n")
print("支持 () [] {} 且三者没有优先级区别")
print(" · 例如: (2 / (2 * (3 + 2) ^ 3)) 等价于 {2 / [2 * (3 + 2) ^ 3]}", end="\n\n")
print("输入的范围是以冒号分隔的闭区间")
print("不输入默认为 [-200, 200]")
print(" · 例如: `Range (l:r): 1:4` 可以代表 1 2 3 4", end="\n\n")

print("试试输入这几个表达式:")
print(" · int(x * 0.01 + 0.5) / 0.01")
print(" · $randint(x - 100, x + 100) * #sin(x * 100)")
print("\n")
print("注意太过复杂的表达式可能会让程序卡死!")
exp = input("f(x) = ")
inp = input("Range (l:r): ")
vld = input("process validation (n): ")

if inp.strip() == "":
    rng = [-200, 200]
else:
    rng = list(map(int, inp.split("|")))

tt.penup()
for x in range(rng[0], rng[1] + 1):
    e = utils.RawExpression(exp)
    print(x, e.bake(x, vld == "Y"))

    down = True
    if x == -200:
        down = False
    utils.draw_point(x, e.bake(x, vld != "n"), down)

tt.done()
