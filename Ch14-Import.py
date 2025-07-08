#ch15匯入四種方式
import math_utils
ansadd=math_utils.add(20,14)
ansmul=math_utils.multiply(20, 14)
print(f"相加等於{ansadd}\n相乘等於{ansmul}")

from math_utils import add,multiply
ansadd=add(18,9)
ansmul=multiply(18, 9)
print(f"相加等於{ansadd}\n相乘等於{ansmul}")

import math_utils as mus
ansadd=mus.add(12,5)
ansmul=mus.multiply(12, 5)
print(f"相加等於{ansadd}\n相乘等於{ansmul}")

from math_utils import*
ansadd=add(3, 45)
ansmul=multiply(3, 45)
print(f"相加等於{ansadd}\n相乘等於{ansmul}")
#*語法會匯入模組中非底線(_)開頭成員。但不建議在正式中使用，因為有可能覆蓋現有變數或函式，並降低程式碼的可讀性。

#ch14
#math 模組：提供各種數學運算相關的函式與常數。
import math

# 計算圓面積
radius = 5
area = math.pi * math.pow(radius, 2)  # math.pow(x, y) 計算 x 的 y 次方
print(f"半徑為 {radius} 的圓面積是: {area:.2f}")

# 計算平方根
num = 144
sqrt_num = math.sqrt(num)
print(f"{num} 的平方根是: {sqrt_num}")


#random 模組：用於生成偽隨機數，常用於模擬、遊戲或抽樣。
import random

# 從 1 到 100 之間隨機選一個整數
random_integer = random.randint(1, 100)
print(f"隨機整數: {random_integer}")

# 從列表中隨機選一個元素
options = ["石頭", "剪刀", "布"]
choice = random.choice(options)
print(f"電腦出拳: {choice}")

# 將列表順序隨機打亂
deck = ["A", "K", "Q", "J"]
random.shuffle(deck)
print(f"洗牌後的順序: {deck}")


#sys 模組：提供存取由Python直譯器使用或維護的變數和函式的方法，例如處理命令列參數。
import sys
# 讀取命令列參數
# 在終端機執行: python your_script.py arg1 arg2
print(f"腳本名稱: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"第一個參數: {sys.argv[1]}")


#建立、使用自訂模組
# main_game.py
import card_utils
import random

# 產生一副牌
deck=list(range(0,52))
random.shuffle(deck)
# 發前三張牌
for i in deck[0:3]:
    colorid=deck[i]
    color=card_utils.get_color(colorid)
    value=card_utils.get_value(colorid)
    print(f"花色{color}；數字{value}")

#------------------------------------------------------------------------------

#1.圓形面積計算：讓使用者輸入圓的半徑，然後使用 math 模組計算並輸出其面積與周長，結果格式化到小數點後兩位
import math

try:
    r=float(input("請輸入半徑"))
    if r < 0 :
        print("請勿輸入負數")
    else:
        a=math.pi*math.pow(r,2)
        l=math.pi*r*2
    print(f"面積為{a:.2f}")
    print(f"周長為{l:.2f}")
except ValueError:
    print("請輸入有效數字")
    
#------------------------------------------------------------------------------

#2.自訂工具模組：建立一個名為 string_tools.py 的模組，其中包含一個函式reverse_string(s)用於反轉字串。
#然後在另一個檔案中匯入並使用它。
import string_tools

string1="alewqq123"
string2=string_tools.reverse_string(string1)
print(string2)

#------------------------------------------------------------------------------

#3.隨機抽獎程式：建立一個參與者名單，使用 random 模組隨機抽出一名幸運得主。
import random

names=["一號","二號","三號","四號","五號","六號"]
winner=random.choice(names)

print(winner)

#------------------------------------------------------------------------------

#4.歐式距離計算：讓使用者輸入兩個點的座標(x1,y1)和(x2,y2)，然後計算兩點間距離，保留小數點後四位。
#歐式距離公式：sqrt{(x1-x2)^2 + (y1-y2)^2}
import math

sx1, sy1=input("輸入一座標，以空白分隔").split()
x1,y1=(float(sx1),float(sy1))
sx2, sy2=input("輸入另一座標，以空白分隔").split()
x2,y2=(float(sx2),float(sy2))

long=math.sqrt((x1-x2)**2+(y1-y2)**2)
print(f"距離為{long:.4f}")

#------------------------------------------------------------------------------

#5.簡易骰子模擬器：模擬擲一顆六面骰子 10 次，並印出每次的結果。
import random

for i in range(0,10):
    randomdice=random.randint(1,6)
    print(randomdice)
    
#------------------------------------------------------------------------------

#6.建立套件並使用： 建立一個名為 mymath 的套件，其中包含一個 operations.py 模組
#，該模組有一個 add(a, b) 函式。然後在套件外部的腳本中呼叫此函式。
#資料夾結構：
#project/
#├── main.py
#└── mymath/
#    ├── __init__.py
#    └── operations.py

#mymath/__init__.py: (可以是空檔案)
#mymath/operations.py:
def add(a, b):
    return a + b

#main.py:
from mymath.operations import add

result = add(5, 3)
print(f"5 + 3 = {result}")

#------------------------------------------------------------------------------

#7.列表去重：給定一個列表 a = [1, 2, 3, 2, 1, 5, 6, 5]，請寫出至少兩種方法將其去重複的。
a = [1, 2, 3, 2, 1, 5, 6, 5]

# 方法一：使用 set
b=list(set(a))
print(b) # 順序可能改變

# 方法二：使用字典的 fromkeys (Python 3.7+ 保持插入順序)
b2 = list(dict.fromkeys(a))
print(f"方法二 (dict.fromkeys): {b2}")

#------------------------------------------------------------------------------

#8.命令列平方計算器：撰寫一個程式，它接收一個從命令列傳入的數字，並印出該數字的平方

#------------------------------------------------------------------------------

#9.字串格式化輸出：讓使用者輸入四個字串，並按照指定的對齊方式將它們格式化輸出成兩行兩列
a = input("輸入第一個字串: ")
b = input("輸入第二個字串: ")
c = input("輸入第三個字串: ")
d = input("輸入第四個字串: ")

print("--- 右對齊 ---")
print('|{:>10s} {:>10s}|'.format(a, b))
print('|{:>10s} {:>10s}|'.format(c, d))

print("--- 左對齊 ---")
print('|{:<10s} {:<10s}|'.format(a, b))
print('|{:<10s} {:<10s}|'.format(c, d))

# format() 方法的一個應用，> 表示右對齊，< 表示左對齊，10s 表示佔用 10 個字元的寬度來顯示字串 