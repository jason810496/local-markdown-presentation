<!--  slide start  -->

# Python Tutorial 2 🐍
## Chapter 2

---

## 📍 `GMJH`
#### ⏱ `2023/07/10` ~ `2023/07/13`

---

## Today Topic
- loop
    - while
    - for


---

# Before we start ... 

----

## Slido 

- **線上匿名提問**
    - 問都問 🫵
- [present link](https://wall.sli.do/event/v4NmQd5VwgA4rBrStRi4fk?section=19f4a706-900d-45a0-87e1-46b0ac1176c3)
- [admin link](https://admin.sli.do/event/v4NmQd5VwgA4rBrStRi4fk/polls)


---

# Tools ⚙️

----

## Replit

- Online IDE
    - [replit.com](https://replit.com/)
![](https://hackmd.io/_uploads/Syc6WS_F3.png)

---

# Warm up 🔥

----

# input() , print()

----

# Data types

----

# X = X + 1

----

# 特別的運算子

<!-- ----

## Kahoot

[Warm up 🧠](https://create.kahoot.it/my-library/kahoots/9c573301-540f-4546-9b3e-c9a4d1adc942) -->

----

## if / else 

---

## Loop

----

如何讓程式解決「重複」的工作呢？

----

就要用到「迴圈」這個語法

----

## 迴圈 Loop
- while loop
- for loop

---

## while 


----

用英文來看：

**當** ... 時


----

## while 語法

```python3
while 條件:
    要執行的程式
```

當符合 `條件` 時 <br> 就會重複跑過縮排區塊的程式

```python3!
while True:
    print("ouo")
```

----

## 如何強制停止程式

<br>

當我們不小心寫出無窮迴圈時
要用 `ctrl + c` 停止程式！

----

## while 範例

跑 `n` 幾次

```python3!
n = 10
i = 0
while i<n:
    print(i)
    i=i+1

print("i after while" , i )
```

----

## while 練習：2 的倍數


用 `while` 印出
`0` ~ `100` 所有 `2` 的倍數

----

## while 練習：猜數字改寫

把昨天的「猜數字」加上 `while`
讓程式跑到**猜中**為止

沒猜對的話：
就提示大於、小於

----

## while 練習：3n+1 循環問題

![](https://hackmd.io/_uploads/r1zedInK3.png)
- `n` 如果是 `奇數` : 
    - `n = 3*n + 1`
- `n` 如果是 `偶數` : 
    - `n = n / 2`
- 當 `n` 是 `1` 時 : 
    - 程式停止


----

## while 搭配 input 

[zerojudge d070](https://zerojudge.tw/ShowProblem?problemid=d070)
- 我們已經會判斷閏年了
- 不過這次程式需要一直讀入 `year` <br> 直到 `year` 是 `0` 為止

---

## for

----

一種通常將 `i` 當做變數的迴圈

----

通常用於明確知道要跑 `n` 次

----

## for 語法

```python
for i in range(10):
    print( i )
```

要注意 `for` 的 `range` 的起始值還有結尾！！！

----

## for 語法

```python
for i in range(n):
    print( i )
```

- `i` 預設都由 `0` 開始
- `i` 不會跑到 `n` 
    - 可以看成在判斷 `i < n`

----

## for 小練習

輸入一個變數 `n` 並讓程式輸出 `1` ~ `n`
```python 
n = int(input("enter a number"))
# ...
```

----

## for 語法變化

`range(起始,結尾)` 
並不包含 `結尾` !!!

```python3!
for i in range(3,7):
    print(i)

```

----

## for 練習-階層

輸入 `n` 並輸出 `n` 階層

階層定義：
- 由 `1` 乘到 `n`
- `3!` = `6`
- `4!` = `24`
- `5!` = `120`

----

## for 練習-判斷質數

要如何判斷質數呢？

Hint : 
- 質數的定義
- 跟取餘數有關

---

## nested loop

----

有提過巢狀 if / else

那當然也有巢狀迴圈

----

也記得注意縮排！！！

----

## Example 

```python3
for i in range(10):
    for j in range(10):
        print( f"({i},{j})" )
```

----

## 巢狀迴圈練習-9x9乘法表

嘗試用巢狀迴圈印出 9x9 乘法表


----

## 巢狀迴圈練習-列出因數

輸入 `n` 並印出 `1` ~ `n` 所有數字各自的因數



