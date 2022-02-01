# function_visualizer

Let the turtle draw images according to the func exp you typed.

## Inputs

- 输入的范围是以冒号分隔的闭区间  
  不输入默认为 `[-200, 200]`

  例如:

  - `Range (l:r): 1:4` 可以代表 `1 2 3 4`

- 一般不需要阻止自动检查表达式  
  默认为开启

  例如:

  - `process validation (n): n` 会关闭自检  
    因此如果表达式在解析过程出错会以报错的形式输出在控制台

## Attentions

如果计算出错画出来的是红线  
通常情况下只有在值不存在时会出现红线  
正常应该是默认的黑线

注意太过复杂的表达式可能会让程序卡死!

## Usages

- 使用 `<>` 代替开平方

  例如:

  - `<2>` 表示 `√2`

- 幂运算使用 `^` 号
  或使用 Python 内建的 `**` 运算符

  例如:

  - `2 ^ 4` 等价于 `2 ** 4`

- 默认导入了 `math` 模块  
  使用 Python 语法可以使用模块内的所有函数  
  或者使用 `#函数名()` 的格式来直接引用模块内的函数

  例如:

  - `math.pow(5, 3)` 表示 5 的 3 次方
  - `#ceil(1.1)` 会被解释为 2 且等价于 `math.ceil(1.1)`

- 同样导入了 `random` 模块  
  与 `math` 模块同理但格式为 `$函数名()`
- 支持 `()` `[]` `{}` 且三者没有优先级区别

  例如:

  - `(2 / (2 _ (3 + 2) ^ 3))` 等价于 `{2 / [2 _ (3 + 2) ^ 3]}`

## Try

试试输入这几个表达式:

- ```
  int(x * 0.01 + 0.5) / 0.01
  ```
- ```
  $randint(x - 100, x + 100) - #sin(x * 100)
  ```
