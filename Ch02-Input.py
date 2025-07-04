# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 10:25:26 2025

@author: Admin
"""

#ex01:
#接收使用者輸入的年齡
age_str = input("請輸入您的年齡: ")

# 將字串轉換為整數
try:
    age_int = int(age_str)
    print(f"您明年就 {age_int + 1} 歲了。")
except ValueError:
    print("輸入無效，請輸入數字。") # 處理使用者輸入非數字的情況

#--------------------------------------------------------------------

#ex02
#處理多個輸入 若要在一行內接收多個由特定符號（如空格）分隔的輸入，
#可以結合使用 input() 和字串的 split() 方法 [8]。

# 接收三個以空格分隔的名字
name1, name2, name3 = input("請輸入三個名字，以空格分隔: ").split()

print('名字1:', name1)
print('名字2:', name2)
print('名字3:''\n', name3)

#--------------------------------------------------------------------

#ex03
#方法一 f-string (格式化字串字面值): 這是目前最推薦的方法，語法簡潔直觀。
#在字串前加上 f 或 F，並將變數或表達式放入大括號 {} 中 。

#方法二 str.format() 方法: 一種功能強大且靈活的格式化方式，透過 {} 作為佔位符。

#方法三 % 運算子:這是源自C語言的傳統格式化方法，雖然仍可使用，但在新專案中較少推薦。

# 範例：格式化輸出
quantity = 3
totalMoney = 1000
price = 450

# 使用 f-string (推薦)
print(f"我有 {totalMoney} 元，可以買 {quantity} 個足球，每個價格為 {price:.2f} 元。")

# 使用 str.format() 方法
statement = "我有 {1} 元，可以買 {0} 個足球，每個價格為 {2:.2f} 元。"
print(statement.format(quantity, totalMoney, price))

# 使用 % 運算子
print("我有 %d 元，可以買 %d 個足球，每個價格為 %.2f 元。" % (totalMoney, quantity, price))

#--------------------------------------------------------------------

#第1題：簡易 BMI 計算機：讓使用者輸入身高（單位：公分）和體重（單位：公斤）
#程式會計算輸出BMI，結果保留小數點後一位。BMI 公式：體重(公斤) / (身高(公尺) ** 2)

try:
    h100=float(input("請輸入身高？"))
    h=h100/100
    w=float(input("請輸入體重？"))
    if h <= 0 or w <= 0 :
       print("體重身高請輸入正數")
    else:
       bmi=w/(h**2)
       print(f"您的 BMI 是: {bmi:.2f}")
except ValueError:
    print("輸入無效，請確保輸入的是數字。")
    
#--------------------------------------------------------------------

#範例 2：字串反轉輸出 問題描述： 讓使用者輸入一個字串，程式將其反轉後輸出。
# 實作範例 2：字串反轉輸出
user_input = input("請輸入一個字串: ")
reversed_string = user_input[::-1]
print(f"反轉後的字串是: {reversed_string}")

#--------------------------------------------------------------------

#範例 3：簡易計算機：接收輸入的兩個數字和一個運算子(+、-、*、/)然後執行運算並輸出結果。

try:
    n1, n2=(input("輸入兩個數字")).split()
    m=input("請輸入四則運算子之中一個+，-，*，/：")
    if m == "+":
        print(int(n1)+int(n2))
    elif m == "-":
        print(int(n1)-int(n2))
    elif m == "*":
        print(int(n1)*int(n2))
    elif m== "/":
        if int(n2) == 0:
            print("錯誤，第二數字不可輸入0")
        else:
            print(int(n1)/int(n2))
    else:
        print("錯誤運算子")
except ValueError:
    print("輸入無效數字")

#--------------------------------------------------------------------

#範例 4：製作使用者名片：接收使用者姓名、電子郵件和電話號碼，然後以整齊的格式輸出成一張名片。
# 實作範例 4：製作使用者名片
name = input("姓名: ")
email = input("電子郵件: ")
phone = input("電話號碼: ")

print("\n" + "="*30)
print(f"姓名: {name}")
print(f"郵件: {email}")
print(f"電話: {phone}")
print("="*30)

#--------------------------------------------------------------------

#範例 5：接收浮點數列表 要求使用者輸入5個浮點數，將它們儲存在一個列表中，最後印出該列表

# 實作範例 5：接收浮點數列表
numbers = []
print("請輸入 5 個浮點數:")

for i in range(0,5):#迴圈從i 開始，到5，也可用range(0,5)→(0+1 1+1 2+1 3+1 4+1)
    while True:
        try:
            item = float(input(f"請輸入第 {i+1} 個數字: "))
            numbers.append(item) #append有遞增用意，在此處從1到5
            break # 輸入成功，跳出內部 while 迴圈
        except ValueError:
            print("輸入無效，請重新輸入一個浮點數。")

print("您輸入的列表是:", numbers)

#內迴圈，可以依序出現不用一次輸入
#內迴圈的Try測試，可避免隨意輸入錯誤字元

#--------------------------------------------------------------------

#範例 6：建立一個簡單的互動式選單提供三個選項，根據使用者的選擇執行不同操作，直到使用者選擇退出

while True:
    print("'\n'輸入選單")
    print("1.說哈囉")
    print("2.算平方")
    print("3.退出")
    
    point=input("請輸入選項")
    
    if point == "1":
        print("哈囉")
    elif point == "2":
        try:
            w=int(input("請輸入一個數字"))
            print(w**2)
        except ValueError:
            print("輸入無效請重新輸入")
    elif point=="3":
        print("再見")
        break
    else:
        print("無效輸入請重來")

#--------------------------------------------------------------------

#範例 7：格式化輸出對齊 問題描述： 假設有三個商品及其價格，
#請使用 f-string 的對齊功能，將它們整齊地以表格形式輸出。
fruits={"蘋果":25,"香蕉":120,"山竹":50}

print(f"{'商品':<8} {'價格':<1}")
for item, price in fruits.items():
    print(f"{item:<8} | {price:>1}")

#--------------------------------------------------------------------

#範例 8：設計一個密碼驗證機制，使用者最多有三次機會輸入正確的密碼 "Python123" 

times=3
for i in range(times):
    password=input("輸入密碼")
    if password == "Python123":
        print("歡迎進入")
        break
    else:
        print(f"密碼錯誤，剩下{times-i-1}次機會")
else:
    print("次數已達上限，鎖定")
    
#--------------------------------------------------------------------

#範例 9：讓使用者輸入一個英文句子，程式計算並輸出該句子包含多少個單字
    
sentence=input("輸入一段英文句子")
sentence_input=sentence.split()
length=len(sentence_input)
print(f"英文句子有{length}個字")

#--------------------------------------------------------------------

#範例 10：百分比顯示 問題描述： 要求使用者輸入分子和分母，計算其百分比，並以 "75.50%" 的格式輸出
son=float(input("請輸入分子"))
mom=float(input("請輸入分母"))

try:
    if mom == 0:
        print("請重新輸入分母，禁止為0")
    else:
        ans=(son/mom)*100
        print(f"答案是：{ans:.2f}%")

except ValueError:
    print("重來")
    
    
    
son = float(input("請輸入分子："))

while True:
    mom = float(input("請輸入分母："))
    if mom == 0:
        print("❌ 錯誤：分母不能為 0，請重新輸入。")
    else:
        ans = (son / mom) * 100
        print(f"✅ 百分比是：{ans:.2f}%")
        break


