# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 11:41:03 2025

@author: Admin
"""

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"目前的水果: {fruit}")

message = "Python"
for char in message:
    print(char)
    
#與print不同，for可以自動增加次數全部印出
#若要限制次數或位置，可用range函數

# 執行 5 次，i 的值依序為 0, 1, 2, 3, 4
for i in range(5):#第1個到第5個"之前"
    print(i)
# i 的值依序為 1, 2, 3, 4
for i in range(1, 5):
    print(i)
# i 的值依序為 1, 3, 5, 7, 9
for i in range(1, 10, 2):#控制遞增遞減因子
    print(i)

numbers = [11, 13, 17, 19]
for num in numbers:
    # 假設我們要找第一個偶數
    if num % 2 == 0:
        print(f"找到第一個偶數: {num}")
        break
else:
    # 只有在迴圈跑完都沒找到偶數時才會執行
    print("列表中沒有偶數")

    
# 1. 初始化計數器
i = 1
# 2. 條件判斷
while i < 5:
    print(i)
    # 3. 更新計數器
    i += 1
    
    
while True:
    user_input = input("您覺得無聊嗎？(輸入 'y' 離開): ")
    if user_input.lower() == 'y':
        print("好吧，去休息一下吧！")
        break
    else:
        print("那我們繼續...")
        
i = 1
while i < 4:
    i += 1
    print(i)
else:
    print("迴圈正常結束，沒有被 break 中斷")
    

#經典範例：九九乘法表 九九乘法表是理解巢狀迴圈運作方式的最佳範例 [9, 14, 17, 20]。
# 外層迴圈控制被乘數 (i)
for i in range(1, 10):
    # 內層迴圈控制乘數 (j)
    for j in range(1, 10):
        # 使用 f-string 格式化輸出
        # end='  ' 讓 print 不換行，並以兩個空格分隔
        print(f"{i}x{j}={i*j:<2}", end='  ')
    # 內層迴圈跑完後換行
    print()

#--------------------------------------------------------------------

#練習一：計算累計總和 題目：讓使用者輸入一個正整數 n，計算從 1 到 n 的所有數字總和
try:
    n=int(input("輸入正整數"))
    if n < 0:
        print("請輸入正整數")
    else:
        sum=0 # 初始化一個變數來儲存總和
        for i in range(1,n+1,1): # 使用for迴圈和range函數來遍歷1到n，注意要寫n+1
            sum += i
            print(sum)
except ValueError:
    print("輸入無效請重新輸入")

#--------------------------------------------------------------------

#練習二：印製星號金字塔 題目：讓使用者輸入一個整數n，印出一個高度為n層的星號金字塔
n=int(input("輸入正整數"))
for i in range(1,n+1):
    print("*")*i
    
n = int(input("請輸入金字塔的高度: "))
    # 外層迴圈控制行數，從 1 到 n
for i in range(1,n+1):
        # 計算每行需要的空格數
        # 第 i 行前面有 (n - i) 個空格
    spaces = ' ' * (n - i)
        
        # 計算每行需要的星號數
        # 第 i 行有 (2 * i - 1) 個星號
    stars = '*' * (2 * i - 1)
        
        # 組合空格和星號並印出
    print(spaces + stars)

#--------------------------------------------------------------------

#練習三
#設計一個使用者登入程式，使用者有三次機會輸入正確的帳號(root)和密碼(1234)
#成功則顯示歡迎訊息並結束，失敗三次則鎖定帳戶

acc="root"
pas="1234"
times=3
tries=0
while tries<times:
    intacc=input("帳號：")
    intpas=input("密碼：")
    tries += 1
    if intacc==acc and intpas==pas:
        print("歡迎使用者")
        break
    else:
        print(f"輸入錯誤，還有{times - tries}次機會")
    if tries==times:
        print("失敗三次已鎖定帳戶")
# 另一種寫法是使用 while-else 結構
# else:
#     print("嘗試次數過多，帳戶已鎖定！"

#--------------------------------------------------------------------

#第一題：印出前 10 個自然數
for i in range(1,11):
    print(i)
    
i = 1
while i <= 10:
    print(i)
    i += 1

#--------------------------------------------------------------------

#第二題：印製數字圖案
n=int(input("輸入一整數"))
out=" "
for i in range(1,n+1):
    out = out + str(i)
    print(out)

#--------------------------------------------------------------------

#第三題：計算數字中的位數
n=int(input("輸入任意數字"))
nn=abs(n)#先取絕對值
nnn=len(str(nn))
print(nnn)
# 不適合處理浮點數（例如 12.34 會算錯）

#數學除法，除已10
n=int(input("輸入一數字"))
n=abs(n)
dig=0
if n==0:
    dig=1
else:
    while n>0:
        n//=10
        dig+=1
    print(f"{dig}位數")

#--------------------------------------------------------------------

#第四題：反向印出列表
list1 = [10, 20, 30, 40, 50]
# 方法一：使用 reversed()
for item in reversed(list1):
    print(item)

# 方法二：使用索引
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
    
#--------------------------------------------------------------------

#第五題：尋找質數(2~100)
#質數判斷：只需檢查到該數的平方根，無法被整除時
print("2 到 100 之間的質數有:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
    
#--------------------------------------------------------------------

#第六題：費波那契數列

#--------------------------------------------------------------------

#第七題：猜數字遊戲

import random
target_number = random.randint(1, 100)
guess = 0
print("猜數字遊戲開始！(1-100)")
while guess!=target_number:
    guess=int(input("猜一數字"))
    if guess>target_number:
        print("太高了")
    elif guess<target_number:
        print("太低了")
    else:
        print(f"答對，數字就是{guess}")

#--------------------------------------------------------------------

#第八題：過濾列表元素
#過濾列表元素：給定列表 numbers = [12, 75, 150, 180, 145, 525, 50]
#遍歷此列表並印出符合以下所有條件的數字：
#(1) 可被 5 整除 (2) 如果數字大於 150，則跳過 (3) 如果數字大于 500，則停止迴圈
      
number = [12,75,150,180,145,525,50]
for i in number:
    if i > 150:
        continue
    if i > 500:
        break
    if i%5 ==0:
        print(i)
        
#--------------------------------------------------------------------

#第九題：計算奇偶數個數
#讓使用者輸入一串以逗號分隔的數字（例如 "1,2,3,4,5,6"），計算其中奇數和偶數的個數。

n=input("輸入一串斗號分隔的數字")
nn=n.split(",")
even=0
odd=0
for i in nn:
    num=int(i.strip()) # strip() 去除可能存在的空格
    if num%2==0:
        even+=1
    else:
        odd+=1
print(f"奇數有{odd}個，偶數有{even}個")
    
user_input = input("請輸入一串以逗號分隔的數字: ")
numbers_str = user_input.split(',')
even_count = 0
odd_count = 0
for s in numbers_str:
        num = int(s.strip()) # strip() 去除可能存在的空格
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
print(f"偶數個數: {even_count}")
print(f"奇數個數: {odd_count}")

#--------------------------------------------------------------------

#第十題：建立字典
#給定兩個列表 keys = ['a', 'b', 'c'] 和 values = [1, 2, 3]
#使用迴圈建立一個字典 {'a': 1, 'b': 2, 'c': 3}        