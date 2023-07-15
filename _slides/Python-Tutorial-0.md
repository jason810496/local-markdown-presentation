
# Python Tutorial 0 🐍
## Chapter 0

---

## 📍 `GMJH`
#### ⏱ `2023/07/10` ~ `2023/07/13`

----

## Basic Topic
- syntax
- containers
- class
- function
- module

----

## Labs
- console program
- online judge

----

## Advances Topic 
- data visualization
- web crawler
- web server

---

# Before we start ... 

----

## Slido 

- **線上匿名提問**
    - 問都問 🫵
- [present link](https://wall.sli.do/event/593m6SKUqgmJT87DYnZNX4?section=554b011b-ff73-4167-b206-60c4043145f6)
- [admin link](https://admin.sli.do/event/593m6SKUqgmJT87DYnZNX4/polls)


----

## 1. About me
## 2. Tools
## 3. Warm up

---

# About me 👋


----





## Jason


----



### 成大資工 大一
- NCKU CSIE
- 全國大專電腦軟體設計競賽
- GDSC
- 架系統
- 打工仔
- ~~拔草~~


----

### 武陵高中
- WLSH
- 資訊社社長
- 資訊學科能力競賽
- 高三開始搞開發
- ~~打工仔~~

----


### GMJH
- 物理老師是 PH 💯
- 完全沒碰過 code

----


### 我碰過什麼
- Competitive Programming
- Frontend
- Backend
- CTF (web security)
- Git workflow 
- Linux 

----

**問都問** 🙌

---

# Tools ⚙️


----

## Development Setup 

設定我們的開發環境！
- VSCode
    - IDE (整合開發環境)
    - https://code.visualstudio.com/download
- Python
    - https://www.python.org/downloads/

[安裝教學 🔗](https://hackmd.io/@smallshawn95/vscode_write_py)

----

## Replit

- Online IDE
    - （ 如果剛剛有成功弄好環境的可以不用
![](https://hackmd.io/_uploads/Syc6WS_F3.png)

----

## zerojudge
- 全台最知名的 Online Judge
    - 所有初學者應該都要來寫過！
- https://zerojudge.tw/
    - 先註冊一下

---

# Warm up 🔥

----

## Kahoot

[Warm up 🧠](https://create.kahoot.it/my-library/kahoots/9c573301-540f-4546-9b3e-c9a4d1adc942)

---

# About Python

----

## Features 

----

### 語法簡單 好上手（很口語化）

```python
print("Hello World!")
a = 1
bucket = []
```

----

### 很多第三方函式庫
- ![](https://hackmd.io/_uploads/ryKU6W_K3.png)
- **DRY** principle
    - **D**on't **r**epeat **y**ourself


----

### 熱門 packages

- AI : 
    - NP , PD , TF , Keras , Pytorch
- Web : 
    - Flask , FastAPI , Django

----


### 熱門 packages (AI)

![](https://hackmd.io/_uploads/H1vSC-dt2.png)

----

### 熱門 packages (Web)

![](https://hackmd.io/_uploads/S1k2gf_tn.png)


----

### 執行速度 ？

![](https://hackmd.io/_uploads/r1Yv1GuK2.png)

----

### 執行速度

其實不快！
應該說是**非常慢** 🐢

----


### 熱門程度

{%youtube GVmeP21x3iM%}

https://youtu.be/GVmeP21x3iM

---

# Summary of Python

----

## Pros
- 語法簡潔
- 快速開發
- 大量第三方套件
- 廣大社群、資源
- 跨平台

----

## Cons
- 執行速度慢
- 無記憶體控管

----

無論如何

每個語言都有優缺點和適用的場域

**Python** 仍是目前的主流語言 ✅

---


# Python syntax


---

## comment

----

## comment

在寫任何一行 code 之前

先學會要怎麼寫註解！

~~不然寫完過三天就看不懂了~~

----

## single line comment

```python
print("Hello world!")
# 輸出 Hello world! , 雙引號不會跟著輸出 , 我寫的第一行 code 
# 第二行
```

----

## multiple line comment

```python
print("Hello world!")
'''
會輸出：
Hello world!
雙引號不會跟著輸出
這是我寫的第一行 code 



空了好多行，再一行
'''
```

---

## stdout 

----

## Output Example

```python
print("This is an output with newline")
```
( 預設就會換行 )

----

## Print with different data type

- 不只能輸出「字串」
```python
print(3.14)
print(111)
print(False)
```

----

## Print multiple variables

- 可以用 `,` 分開要輸出的東西
```python
print("Pi =",3.14)
```
( 預設會用空白隔開 )

----

## Customize end char

- 如果我不想要結尾換行呢？
```python
print("End with empty string.",end="")
```

- 可以使用 `end="你想要的結尾"`

----

## Customize separator

- 如果我不想要用空白分隔呢？
```python
print(1,2,3,sep=",")
```
- 可以使用 `sep="你想要的結尾"`
- 這邊改成用 `,` 分隔

----

## Lab

- d483. hello, world
[Zerojudge d483](https://zerojudge.tw/ShowProblem?problemid=d483)

---


## stdin

----

## input()

- 會等使用者輸入再繼續跑
- 讀進來都是字串

----

## Input example

```python
a = input()
print( type(a) ) # str
```

----

## Input with prompt

```python
user = input("Enter a name:")
food = input("Enter a type of food :")

print(user,"is eating",food)
```

----

## Lab : on your own

三角形面積計算機
- 讓使用者輸入兩個變數 `width` `height`
- 輸出三角形的面積

Example Input:
```
5
4
```
Example Output:
```
10
```

----

## Lab : Zerojudge a001

[a001. 哈囉](https://zerojudge.tw/ShowProblem?problemid=a001)

---

### variables & data types & operator

---

## variables

----

## variables：變數

----

## data type：資料型態

----

## variables 變數
- 存放資料
- Python 會幫我們判別變數型態

----

## variables Naming 變數命名
- 不能重複命名
- 不能用數字開頭
- 不能用 `+` `-` `*` `/` `%` `&` 連接（ 底線 `_` 可以）
- 不能使用保留字
    - `while` `if` `else` ...


----

## Correct Naming Example 

```python
a=1
b =3.210
c123 = False
__12_Jo_= "string obj"
signleQuoteStr = '123'
```

----

## Mistake Naming Example

```python
123ouo = 1
a*b-c = d
if = None
```

----

## Naming Style
- Camel Case
    - `hasCar` `coolBlueBigCar`
- Snake Case
    - `has_car` `cool_blue_big_car`



----

## readable variables naming

盡量把變數命名的有意義！


----

## Bad example 

```
a=1
ouo="User"
c=False
__123=456
# .... -> confusing 🤯
```

----

## Good example

```
count = 1
userName = "User"
hasCent = False
money = 456
```

----

## variable naming for configuration

在專案中用於 **設定相關** 的變數<br>大多會命名成 **底線搭配全大寫**
```python
CLIENT_LIMIT=50
SERVER_NAME="www.jason.com"
WORKER_ENABLE=True
```

----

# Lab
> 練習一下
> 看個例子


---

## data type 

----

## data type 資料型態
Python 基礎的資料型態：
- 文字相關
    - `str`
- 數字相關
    - `int`
    - `float`
- 其他
    - `bool`
    - `byte`
    - `NoneType`

----

## check data type

如何確認資料型態？

----

## check data type

如何確認資料型態
```
print( type(varName) )
```

```
num="123"
print( type(varName) ) # str
```

----


## type casting

如何把「字串」轉乘「整數」呢？

或是

如何把「整數」轉乘「浮點數」呢？

----

## type casting Examples 

```python
num = 123
num_float = float(num)
num_int = int(float('2.79'))
```

---

# operator

----

## operator 運算子
跟一般數學一樣，Python 也可以 `+` `-` `*` `/`

----

## operator example

```python
print(10*5)

a=9
b=7
print(9-7)
```

----

## operator example

```python
print(10*5)

a=9
b=7
print(9-7)
```

----

## divide operator

```python
print(5/3) 
print(5//3) 
print( int(5/3) ) 
```

----

## 除法的陷阱

```python
print(5/3) # 1.6666666666666667
print(5//3) # 1
print( int(5/3) ) # 1
```

----

## 次方

現在 `a` , `n` 兩個變數，要計算 `a` 的 `n` 次方

```python
# try it your self 
```

----

## operator of power

不是 `^` 是 `**` 兩個乘號

```python
print(3**5)
```

----

## mod operator

> 有一個在寫程式很常用到的運算子
> 但國中好像還沒教到
> 不過概念很簡單

----

## 取餘數

math : 

```
a mod b : a/b 的餘數
```

programming : 

```
a%b
```

Example : 
```
16%5 = ? 
99%2 = ?
66%3 = ?
```

----

## operator between different type

不同型態之前可以運算嗎？

----

## Example

```python
print(123*123)
print("123"*123)
print("")
```


----

## X = X + 1

<img src="https://pbs.twimg.com/media/Eq3WEN-U0AMP2Lr.jpg" height="600px"/>

<!-- ![meme](https://pbs.twimg.com/media/Eq3WEN-U0AMP2Lr.jpg) -->

----

## X = X + 1

> 不知道變化
> 就每行先 print 出來看看！


----

## Lab : on your own

輸入 `a` `b` 兩個變數，並輸出以下結果

Example output:
```
a is : 5
b is : 3
The result of a + b is : 8
The result of a - b is : 2
The result of a * b is : 15
The result of a / b is : 1.6666666666666667
The result of a mod b is : 2
The result of a ^ b is : 125
```

----

## Lab : Zerojudge d827

[d827. 買鉛筆](https://zerojudge.tw/ShowProblem?problemid=d827)

---


# Python is an interpreter language

---

## Python 是一個直譯語言 (？

----

Compiled language <br>
vs <br>
Interpreter language

----

編譯語言 <br>
vs <br>
直譯語言

----

## 編譯語言

- 由 Compiler (編譯器) 先把 source code <br> compile 成 binary file (二進位檔)
- C , C++ , Rust

----

## 直譯語言

- 由 Interpreter (直譯器) 一行一行執行 <br>（讀到的當下才轉成 `0`跟`1`）
- Python , Javascript , PHP

----

## 既然 Python 是直譯語言

> 那是不是可以
> 一行一行輸入給直譯器跑 ？

----

## Lab : on your own

來跟 Python Interpreter 玩一下