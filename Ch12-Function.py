#函式的定義:用def關鍵字來定義一個函式。一個完整的函式定義包含以下幾個部分：
#def 關鍵字：宣告這是一個函式定義的開始。
#函式名稱 (Function Name)：一個自訂的、符合變數命名規則的名稱，用以識別此函式。
#參數列表 (Parameters)：置於括號()中，用來接收外部傳入的資料。
#參數可為零個、一個或多個，參數之間以逗號 , 分隔。
#冒號 :：位於參數列表之後，是語法的一部分。
#函式主體 (Function Body)：def行下方，透過"縮排"來表示屬於此函式的程式碼區塊。這裡包含了函式要執行的所有操作。
#文件字串 (Docstring)：可選項目，通常是函式主體的第一行
#使用三重引號 """...""" 包裹，用來說明函式的功能、參數與回傳值。

#e.g.1
def show_greeting():
    """這是一個簡單的函式，用於顯示問候訊息。"""
    print("Hello, 阿昌哥老師!")
show_greeting()

#e.g.2定義矩形面積
def rectangle_area(length,width):
    """
    計算並印出矩形的面積。
    :param length: 矩形的長度
    :param width: 矩形的寬度
    """
    # :param為說明參數的意思
    area = length*width
    print(f"長{length}，寬{width}，面積{area}")
rectangle_area(10,5)

#呼叫函數：需要輸入函數的關鍵字(函數名稱)並輸入相關參數"資料函數"(Arguments)，若無參數可用空白()

#參數
#位置參數 (Positional Arguments) ：呼叫函式時，傳入的資料參數會依照其位置順序，依序對應到函式定義中的參數。
#關鍵字參數 (Keyword Arguments) ：可讀性並避免順序錯誤，呼叫時明確指定參數的名稱。
#使用關鍵字參數時，參數的順序就不再重要了

def student_info(name, student_id, department):
    print(f"姓名: {name}, 學號: {student_id}, 系別: {department}")
student_info(department="資訊",name="ben",student_id=454546)
#順序可以錯誤沒關係

#參數預設值 (Default Arguments) 可以為參數指定一個預設值。如果在呼叫函式時沒有提供該參數的值，
#Python 就會自動使用這個預設值

def greet(name, message="您好"):
    print(f"{name}, {message}!")

greet("王老師") # message 參數使用預設值
greet("李同學", "早安") # message 參數被賦予新值

#可變數量參數 (*args 和 **kwargs) 當不確定函式會接收多少個參數時，可以使用這種特殊的語法。
# *args：將所有多餘的位置參數收集起來，打包成一個元組 "(tuple)"。關鍵為使用星號
# **kwargs：將所有多餘的關鍵字參數收集起來，打包成一個字典 "(dictionary)"

def calculate_sum(*numbers):
    """計算傳入的所有數字的總和"""
    total = sum(numbers)
    print(f"傳入的數字為: {numbers}")
    print(f"總和為: {total}")

calculate_sum(15,45,20)

def print_kwargs(**info):
    print("關鍵字參數有：", info)

print_kwargs(name="Alice", age=25)
print_kwargs(city="Taipei")

#回傳值 (Return Value)：不僅能執行操作，更能將結果「回傳」給呼叫它的地方，以便進行後續的運算。
#return 關鍵字有兩個主要作用：
#1.立即結束函式的執行。
#2.將 return 後方的物件或值傳回。
#如果函式中沒有 return 語句，或者 return 後方沒有任何值，函式會預設回傳一個特殊的值 None

#攝氏轉華氏溫度 這個函式接收攝氏溫度，計算後回傳對應的華氏溫度
def celsius_to_fahrenheit(celsius):
    """將攝氏溫度轉換為華氏溫度並回傳結果"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 呼叫函式並將回傳值存入變數
f_temp = celsius_to_fahrenheit(30)
print(f"攝氏 30 度等於華氏 {f_temp:.2f} 度")

celsius_to_fahrenheit(30) #沒有print，不會印出，但會保留數值

# 回傳值可以直接用於運算
print(f"攝氏 0 度的兩倍華氏溫度是 {celsius_to_fahrenheit(0) * 2} 度")
print({celsius_to_fahrenheit(0) * 2} )

#若不用return
def celsius_to_fahrenheit_print(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"直接印出結果：{fahrenheit}°F")

# 呼叫函式
celsius_to_fahrenheit_print(25)
#若又做其他運算就會錯誤，不能將整團函數作為一個值
print(f"攝氏 0 度的兩倍華氏溫度是 {celsius_to_fahrenheit_print(0) * 2} 度")
print({celsius_to_fahrenheit_print(0) * 2})

#多重回傳值 Python 函式可以一次 return 多個值。
#在底層，會被自動打包成一個元組 (tuple) 回傳。我們可以使用多個變數來接收這些被解包 (unpack) 的值 

#計算最大公因數與最小公倍數 設計一個函式，接收兩個整數，回傳它們的最大公因數 (GCD) 和最小公倍數 (LCM)
import math

def calculate_gcd_lcm(a, b):
    """計算並回傳兩個數的最大公因數gcd與最小公倍數lcm"""
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return gcd, lcm

# 呼叫函式並用兩個變數接收回傳值
common_divisor, common_multiple = calculate_gcd_lcm(12, 18)

print(f"12 和 18 的最大公因數是: {common_divisor}")
print(f"12 和 18 的最小公倍數是: {common_multiple}")


#區域變數 (Local Variables)：在函式內部定義的變數，其生命週期僅限於該函式的執行期間。
#函式執行結束後，區域變數就會被銷毀，無法從函式外部存取。
#全域變數 (Global Variables)：在所有函式之外定義的變數，其作用域是整個程式檔案。任何地方都可以存取它。
#global 關鍵字 如果在函式內部需要修改一個全域變數的值，必須使用 global 關鍵字來明確聲明 [3]。
#範例實作與說明 ex10
counter = 100  # 全域變數

def my_function():
    local_counter = 10  # 區域變數
    print(f"函式內部讀取區域變數: {local_counter}")
    print(f"函式內部讀取全域變數: {counter}")

def modify_global_counter():
    global counter  # 聲明要修改的是全域變數 counter
    counter = 200
    print(f"函式 modify_global_counter 修改後的全域變數: {counter}")

print(f"呼叫函式前，全域變數 counter: {counter}") # 輸出 100
my_function()
# print(local_counter) # 這行會報錯，因為無法在外部存取區域變數

modify_global_counter()
print(f"呼叫函式後，全域變數 counter: {counter}") # 輸出 200

#------------------------------------------------------------------------------

#選擇7
def multiply(n1, n2):
    print(n1 * n2)

value = multiply(3, 4)
#注意！沒有回傳值，雖然會運算，但沒有return給予"value"，只有印出12而已，故value為none

#------------------------------------------------------------------------------
#練習1：華氏轉攝氏溫度轉換
#請撰寫一函式 fahrenheit_to_celsius，接收一個華氏溫度，回傳其對應的攝氏溫度。
#(輸出值請四捨五入至小數點後第二位。提示：攝氏 = (華氏 - 32) * 5/9)

def fahrenheit_to_celsius(fehrenheit):
    celsius = (fehrenheit - 32) * 9/5
    return celsius

ftemp=100
ctemp=fahrenheit_to_celsius(ftemp)
print(f"華氏{ftemp}度為攝氏{ctemp}度")

#------------------------------------------------------------------------------

#練習2：判斷奇偶數
#題目描述：請撰寫一函式 is_even，接收一個整數，如果該整數是偶數則回傳 True，奇數則回傳 False

def is_even(digit):
    if digit % 2 == 0:
        print(True)
    else:
        print(False)

is_even(257)#這邊會得到"答案"(印出在計算機中，但沒有回傳出digit得到的布林值

#應該要用"回傳"布林值
def is_even(digit):
    if digit % 2 == 0:
        return True
    else:
        return False
#或是
def is_even(digit):
    return digit % 2 == 0

is_even(257)

#------------------------------------------------------------------------------

#練習3：繪製星號倒三角形
#題目：請撰寫一函式 draw_inverted_triangle，接收一個整數 n，然後在畫面上印出一個高度為 n 的倒三角形

def draw_inverted_triangle(n):
    """根據輸入的整數 n，印出倒三角形"""
    for i in range(n,0,-1):
        print(i*"*")

draw_inverted_triangle(5)

#------------------------------------------------------------------------------

#練習4：計算階乘
#題目： 請撰寫一函式 factorial，接收一個非負整數 n，回傳 n 的階乘 (n!)

def factorial(n): #不檢查負數的狀況下可寫
    result=1
    for i in range(1,n+1):
        result *= i
    return result

def factorial(n):
    """計算 n 的階乘"""
    if n < 0:
        return "不支援負數"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
factorial(5)
factorial(-5)
       
#------------------------------------------------------------------------------

#練習5：尋找串列表(list)的最大值 (不使用 max())
#題目描述： 請撰寫一函式 find_max，接收一個數字列表，回傳列表中的最大值

def find_max(list1):
    if not list1:
        return False
    
    maxnum=list1[0]
    for i in list1:
        if i > maxnum:
            maxnum = i
    return(maxnum)

listeg=[-1,0,-8]
find_max(listeg)

#也可用arg，但題目改稱輸入多個數字
def find_max(*args):
    if not args:
        raise ValueError("至少要提供一個數字")
    
    max_value = args[0]
    for num in args[1:]:
        if num > max_value:
            max_value = num
    return max_value

#------------------------------------------------------------------------------

#練習6：判斷是否為閏年
#題目：請撰寫一函式 is_leap_year，接收一個西元年份
#如果該年是閏年，則回傳 True，否則回傳 False。閏年規則：能被 4 整除但不能被 100 整除，或者能被 400 整除

def is_leap_year(y):
    if (y%4==0 and y%100!=0) or y%400==0 :
        return True
    else:
        return False

is_leap_year(2010)

#------------------------------------------------------------------------------

#練習7：字串反轉
#題目：請撰寫一函式 reverse_string，接收一個字串，回傳反轉後的新字串

def reverse_string(string):
    return string[::-1]

reverse_string("allem")

#------------------------------------------------------------------------------

#練習8：計算字串中各類字元的個數
#題目：請撰寫一函式 count_chars，接收一個字串，計算並回傳字串中包含的英文字母、數字、空格及其他字元的個數

def count_chars(text):
    letters = 0
    digits = 0
    spaces = 0
    others = 0

    for char in text:
        if char.isalpha():         # 是英文字母
            letters += 1
        elif char.isdigit():       # 是數字
            digits += 1
        elif char.isspace():       # 是空白字元（空格、換行、tab）
            spaces += 1
        else:                      # 其他符號
            others += 1

    return {
        "letters": letters,
        "digits": digits,
        "spaces": spaces,
        "others": others
    }

count_chars("aklfoei455 65i4*-+")

#------------------------------------------------------------------------------

#練習9:選擇排序 (Selection Sort)
#題目描述：請撰寫一函式 selection_sort，接收一個數字串列(list)，並對其進行「原地」升序排序。

def selection_sort(arr):
    """對列表進行選擇排序（原地排序）"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 將找到的最小值與當前位置的元素交換
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        #「交換變數值」的寫法：把 numbers[i] 和 numbers[min_index] 兩個位置的元素 交換值

# 測試函式
my_list = [7, 4, 6, 9, 5, 2]
print(f"原始列表: {my_list}")
selection_sort(my_list)
print(f"排序後列表: {my_list}")

#------------------------------------------------------------------------------

#練習10:猜數字遊戲
#題目描述： 請撰寫一函式 guess_number_game，函式內部會隨機產生一個 0~9 的整數。
#讓使用者有三次猜測機會，如果猜中，顯示「恭喜猜對了！」並結束函式；
#如果三次都沒猜中，則顯示「可惜，答案是 X」。w10 詳解：
import random

def guess_number_game():
    """一個簡單的猜數字遊戲函式"""
    answer = random.randint(0, 9) #randint()：隨機產生一個區間內的數字
    
    for i in range(3):
        try:
            guess = int(input(f"第 {i+1} 次猜測 (0-9): "))
            if guess == answer:
                print("恭喜猜對了！")
                return # 猜對了就直接結束函式 return：直接結束函式 → 不用再用 break
        except ValueError:
            print("請輸入有效的數字。")
            continue # 如果輸入無效，跳過此次猜測

    print(f"可惜，三次都沒猜中。答案是 {answer}")