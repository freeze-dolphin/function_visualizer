import utils
import turtle as tt

print("用法详见仓库 README")
print("仓库地址 https://github.com/freeze-dolphin/function_visualizer")
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
