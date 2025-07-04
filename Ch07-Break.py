# continue 為"跳過"，而非"繼續"
vowels = "aeiou"
for letter in "Hello, World!":
    if letter.lower() in vowels:
        continue  # 如果是母音，跳過本次迭代
    print(letter, end="")

print("\n迴圈已結束。")
#跳過了e,o,o，而非繼續生成

# 範例 1: break 導致 else 不執行
for i in range(1, 6):
    if i == 3:
        print(f"在 {i} 處中斷迴圈")
        break
    print(i)
else:
    print("迴圈正常結束") # 這行不會被執行

print("-" * 20)

for i in range(1, 3): #1、2結束，不引發break
    if i == 3:
        print(f"在 {i} 處中斷迴圈")
        break
    print(i)
else:
    print("迴圈正常結束") # 這行會被執行

print("-" * 20)

# 範例 2: continue 不影響 else 執行
for i in range(1, 6):
    if i == 3:
        print("跳過 3")
        continue
    print(i)
else:
    print("迴圈正常結束") # 這行會被執行

#------------------------------------------------------------------------------

#練習 1：數字篩選器：編寫一個程式，計算 1 到 50 之間所有不是 7 的倍數的數字的總和。

summ=0
for i in range(1,51):
    if i%7 != 0:
        summ += i
    else:
        continue
print(summ)

#------------------------------------------------------------------------------

#練習 2：使用者密碼驗證：設計一個密碼驗證系統，預設密碼為 "password123"；
#讓使用者最多嘗試輸入3次，如果輸入正確，顯示「登入成功」並結束程式；
#如果3次都錯誤，顯示「帳號已鎖定」。

password="password123"

maxim=3
tries=0
while tries < maxim:
    int_pass=input("請輸入一則密碼")
    tries += 1
    if int_pass == password:
        print("登入成功")
        break
    else:
        print(f"密碼錯誤剩下{maxim-tries}次機會")
        if tries == maxim:
            print("達到次數上限，已鎖定")
