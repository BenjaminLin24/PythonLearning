# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 15:09:20 2025

@author: Admin
"""

count = 0
count += 1  # 等同於 count = count + 1，常用於計數器
print(count) # 輸出 1
#迴圈遞增範例

n=int(input("輸入數字"))
while True:
    if n == 25:
        print("end")
        break
    elif n <=25:
        n += 1
        print("restart"+str(n))
    else:
        print("請輸入小於25的數字")
        break
    
while True:
    n = int(input("請輸入小於或等於 25 的數字："))

    if n <= 25:
        while n <= 25:
            if n == 25:
                print("end")
                break
            else:
                n += 1
                print("restart " + str(n))
        break  # 結束外層迴圈
    else:
        print("❌ 請重新輸入一個小於或等於 25 的數字")
        # 沒有用 continue，單純讓它回到 while 頂部

#--------------------------------------------------------------------

#第1題
#圓形面積計算 請撰寫一程式，讓使用者輸入圓形的半徑 (radius)，然後計算並輸出其面積
#圓面積公式為 $Area = \pi \times r^2$

import math
print(math.pi)

radius=float(input("輸入圓半徑"))
area=(math.pi)*radius**2
print(f"面積為{area:.2f}")

#--------------------------------------------------------------------

#2題 
#偶數判斷 請撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數 (even)。

m=int(input("請輸入一正整數"))

if m%2 == 0:
    print(f"{m}為偶數")
else:
    print("奇數")
    
#--------------------------------------------------------------------

#3.題 
#閏年判斷 讓使用者輸入一個西元年份，判斷其是否為閏年 (leap year)。判斷規則：
#可被 4 整除，但不可被 100 整除。
#或者可被 400 整除。

year=int(input("輸入一個西元年"))
a=year%4
b=year%100
c=year%400

if ((a==0)&(b!=0)) or (c==0):
    print(f"{year}是閏年")
else:
    print(f"{year}是平年")

#--------------------------------------------------------------------

#4題
#變數值交換 已知 a = 100, b = 200
#請用一行 Python 程式碼交換 a 和 b 的值，使得 a 變為 200，b 變為 100

a=100
b=200
a,b=b,a

print(a,b)
print(f"交換後: a = {a}, b = {b}")

#--------------------------------------------------------------------

#第5題
#讓使用者輸入攝氏溫度 (Celsius)，並將其轉換為華氏溫度 (Fahrenheit) 後輸出。
#轉換公式為 $F = C \times \frac{9}{5} + 32$

c=float(input("輸入攝氏度"))

f=(c*9/5)+32
print(f'華氏度為：{f:.1f}度')

#--------------------------------------------------------------------

#6.題
#假設某線上商店規定，顧客必須是會員 (is_member = True) 且 
#單次消費金額 (purchase_amount) 超過 1000 元，
#或者 是 VIP 會員 (is_vip = True)，才能享有免運費優惠。

is_member = True
purchase_amount = 100
is_vip = False
if is_member&(purchase_amount >= 1000) or is_vip :
    print("你是vip")
else:
    print("滾！！")

#--------------------------------------------------------------------

#7題
#找出列表中的最大值 給定一個數字列表 numbers = [45, 88, 12, 99, 34]，
#請不要使用內建的 max() 函式，而是透過迴圈和比較運算子找出列表中的最大值。

numbers = [45, 88, 12, 99, 34]
max_val = numbers[0] # 先假設第一個數是最大值

for num in numbers:
    if num > max_val: # 如果找到更大的數
        max_val = num # 就更新最大值
        #45<88變88，88>12維持88，88<99變99，99>34不變，答案為99

print(f"列表中的最大值是: {max_val}")

#--------------------------------------------------------------------

#8題：bmi計算

h=float(input("你得身高"))
w=float(input("你的體重"))
hh=h/100
bmi=w/(hh**2)
print(f"bmi為{bmi:.1f}")

#--------------------------------------------------------------------

#9題
#計算一個三位數正整數的各個位數之和。例如，輸入 345，應輸出 3 + 4 + 5 = 12。

m=input("請輸入一三位數正整數")
sigma=int(m[0])+int(m[1])+int(m[2])
print(sigma)

num = int(input("請輸入一個三位數正整數: "))

# 分解數字
hundreds = num // 100       # 取百位數
tens = (num % 100) // 10    # 取十位數
units = num % 10            # 取個位數

total = hundreds + tens + units
print(f"各位數之和為: {total}")

#--------------------------------------------------------------------

#10題
#範圍檢查 請撰寫一程式，判斷使用者輸入的數字是否落在 1 到 100 的區間內（含 1 和 100）

m=int(input("輸入一正整數"))

if m >= 1 and m <= 100:
    print("我要的")
else:
    print("重來")