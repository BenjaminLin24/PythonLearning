# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 09:09:43 2025

@author: Admin
"""

#例題1：if
score = 100
if score == 100:
    print("你太棒了，滿分！")


#例題2：if-else
age = 17
if age >= 18:
    print("您已成年，歡迎光臨。")
else:
    print("抱歉，您未滿18歲，禁止進入。")
    
    
#例題3：if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"您的成績等級為：{grade}") # 輸出: 您的成績等級為：B


#例題4：判斷大小正負或零
num=float(input("輸入一數值"))
if num == 0 :
    print(f"{num}為零")
elif num >= 0 :
    print(f"{num}為正數")
else:
    print(f"{num}為負數")
    

#例題5：判斷閏年，被4整除但不被100整除，或是被400整除
year=int(input("請輸入一個西元年"))
a=year%4
b=year%100
c=year%400

if (a==0 and b!=0) or c==0 :
    print(f"您輸入的年份:{year}為閏年")
else:
    print(f"您輸入的年份:{year}為平年")


#例題6：巢狀多條件(if條件中還有一個條件)
age=int(input("輸入您的年齡"))

if age < 18:
    print("可以購買兒童票，100元")
else:
    stu=input("是否為學生？(y/n)")
    if stu.lower == "y" : #lower，轉換為小寫，避免輸入值為大寫
        print("可以購買學生票，120元")
    else:
        print("請購買全票，150元")
        

#--------------------------------------------------------------------

#第 1 題
#請撰寫一個程式，讓使用者輸入 1 到 7 的數字，並根據數字印出對應的星期
#（1代表星期一，7代表星期日）。如果輸入的數字超出範圍，則印出 "輸入錯誤，超出範圍"
num=int(input("請輸入1~7其中任一個數字"))

if num == 1:
    print("星期一")
elif num == 2:
    print("星期二")
elif num == 3:
    print("星期三")
elif num == 4:
    print("星期四")
elif num == 5:
    print("星期五")
elif num == 6:
    print("星期六")
elif num == 7:
    print("星期日")
else:
    print("輸入錯誤，超出範圍")

#--------------------------------------------------------------------

#第 2 題
#讓使用者輸入身高（公尺）和體重（公斤），計算其 BMI 值（公式：體重 / 身高²）
#BMI < 18.5: "體重過輕"
#18.5 <= BMI < 24: "正常範圍"
#24 <= BMI < 27: "過重"
#27 <= BMI < 30: "輕度肥胖"
#30 <= BMI < 35: "中度肥胖"
#BMI >= 35: "重度肥胖"

h=float(input("請輸入身高(公分)"))/100
w=float(input("請輸入體重(公斤)"))
bmi=w/(h**2)

if bmi >= 35:
    print(f"您的BMI值為：{bmi:.1f}"+"→"+"體重過重")
elif bmi >= 30: # 不用寫 bmi < 35，因為若不滿足，必已大於等於 35
    print(f"您的BMI值為：{bmi:.1f}"+"→"+"中度肥胖")
elif bmi >= 27:
    print(f"您的BMI值為：{bmi:.1f}"+"→"+"輕度肥胖")
elif bmi >= 24:
    print(f"您的BMI值為：{bmi:.1f}"+"→"+"過重")
elif bmi >= 18.5:
    print(f"您的BMI值為：{bmi:.1f}"+"→"+"正常範圍")
else:
    print(f"您的BMI值為：{bmi:.1f}"+"→"+"體重過輕")

#--------------------------------------------------------------------

#第 3 題：FizzBuzz挑戰
#讓使用者輸入一個整數。如果該數字是 3 的倍數，印出"Fizz"；
#如果是 5 的倍數，印出"Buzz"；
#如果同時是 3 和 5 的倍數，印出 "FizzBuzz"；
#如果都不是，則印出原數字。

n=int(input("請輸入一個整數"))
a=n%3
b=n%5
c=n%15

if c == 0:
    print("FizzBuzz")
elif b == 0:
    print("Buzz")
elif a == 0:
    print("Fizz")
else:
    print(n)

#--------------------------------------------------------------------

#第 4 題
#讓使用者輸入出生年份，程式會印出對應的生肖
#年份除以 12 的餘數。對應關係如下表（以 2008 年鼠年為例，2008 % 12 = 4）
#餘數 0: 猴；餘數 1: 雞；餘數 2: 狗；餘數 3: 豬；餘數 4: 鼠；餘數 5: 牛
#餘數 6: 虎；餘數 7: 兔；餘數 8: 龍；餘數 9: 蛇；餘數 10: 馬；餘數 11: 羊

year=int(input("請輸入一西元年"))
s=year%12

if s == 0:
    print("猴年")
elif s == 1:
    print("雞年")
elif s == 2:
    print("狗年")
elif s == 3:
    print("豬年")
elif s == 4:
    print("鼠年")
elif s == 5:
    print("牛年")
elif s == 6:
    print("虎年")
elif s == 7:
    print("兔年")
elif s == 8:
    print("龍年")
elif s == 9:
    print("蛇年")
elif s == 10:
    print("馬年")
elif s == 11:
    print("羊年")
    
#--------------------------------------------------------------------

#第 5 題：三角形類型判斷
#讓使用者輸入三角形的三個邊長。程式需先判斷這三個邊長是否能構成一個三角形
#條件：任意兩邊之和大於第三邊。如果可以，再判斷是哪種類型的三角形並印出：
#等邊三角形 (Equilateral)：三邊相等。
#等腰三角形 (Isosceles)：任兩邊相等。
#不等邊三角形 (Scalene/Obtuse)：三邊皆不相等。
#如果無法成立，印出 "無法構成三角形"。

l11,l22,l33=input("請輸入三個邊長，並以空格隔開").split()
l1,l2,l3=float(l11),float(l22),float(l33)
print(f"您輸入的邊長為{l1} {l2} {l3}")

if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print("三角形成立！")
    if l1 == l2 and l2 == l3:
        print("等邊三角形！")
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print("不等邊三角形！")
    else:
        print("等腰三角形！") #可以用l1==l2orl2==l3orl3==l1
else:
    print("無法構成三角形")

#--------------------------------------------------------------------

#第 6 題：簡易猜數字
#程式預設一個 1 到 10 之間的秘密數字。讓使用者輸入猜測的數字。
#如果猜對了，印出 "恭喜你，猜對了！"
#如果猜錯了，則提示使用者猜的數字是 "太大了" 還是 "太小了"

sn=5

while True:
    yn=int(input("請任意猜選一個1~10之間的數字"))
    if yn == sn:
        print("恭喜你猜中了")
        break
    elif yn > sn:
        print("太大了在一次")
    else:
        print("太小了再一次")
        

sn = 5  # 正確答案
max_tries = 3  # 最多可以猜 3 次
tries = 0  # 猜的次數累加器

while tries < max_tries:
    yn = int(input(f"請猜一個 1~10 之間的數字（剩下 {max_tries - tries} 次機會）："))
    tries += 1

    if yn == sn:
        print("恭喜你猜中了！")
        break
    elif yn > sn:
        print("太大了，再一次。")
    else:
        print("太小了，再一次。")

if tries == max_tries and yn != sn:
    print(f"很可惜，已經猜了 {max_tries} 次。正確答案是 {sn}。")

#--------------------------------------------------------------------

#第 7 題：季節判斷
#讓使用者輸入月份（1-12），程式根據月份判斷並印出對應的季節。
#3, 4, 5 月:"春天"；6, 7, 8 月:"夏天"；9, 10, 11 月:"秋天"；12, 1, 2 月:"冬天"
#其他輸入: "月份輸入錯誤"

mon=int(input("請輸入一個月份"))

if mon>=3 and mon<=5:
    print("春天")
elif mon>=6 and mon<=8:
    print("夏天")
elif mon>=9 and mon<=11:
    print("秋天")
else:
    print("冬天")

#串列用法
#if month in [3, 4, 5]:
#   print("春天")

#--------------------------------------------------------------------

#第 8 題：折扣計算
#消費金額滿1000元，打9折。消費金額滿3000元，打8折。消費金額滿5000元，打7折。
#請撰寫一個程式，讓使用者輸入消費金額，並計算出折扣後的應付金額。

yen=int(input("消費額輸入"))

if yen>=5000:
    print(f"打7折，折扣後為{int(yen*0.7)}")
elif yen>=3000:
    print(f"打8折，折扣後為{int(yen*0.8)}")
elif yen>=1000:
    print(f"打9折，折扣後為{int(yen*0.9)}")
else:
    print(f"未打折，應付{yen}元")

#--------------------------------------------------------------------

#第 9 題：奇偶數判斷 題目：讓使用者輸入一個整數，判斷該數是奇數還是偶數，並印出結果

num=int(input("輸入一整數"))
if num%2 == 0:
    print("偶數")
else:
    print("奇數")

#--------------------------------------------------------------------

#第 10 題：登入驗證
#設定一組固定的使用者名稱和密碼（例如user和1234）。讓使用者輸入使用者名稱和密碼
#如果兩者都正確，印出 "登入成功！"；否則，印出 "使用者名稱或密碼錯誤。"

name="user"
password="1234"

while True:

    intname=input("請輸入使用者名稱")
    intpassword=input("請輸入密碼")
    if intname==name and intpassword==password:
        print("登入成功")
        break
    else:
        print("使用者名稱或密碼錯誤")