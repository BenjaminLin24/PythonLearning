#try...except...else...finally
#try區塊：將可能引發異常的程式碼放置於此。
#except區塊：try區塊發生異常，Python會"跳過"try"區塊剩餘程式碼，並匹配該異常類型的except區塊執行
try:
    result = 10 / 0
except ZeroDivisionError:
    print("處理錯誤：除數不能為零！") # 這行會被執行(若錯誤種類不對，會向上顯示錯誤)

print("程式繼續執行...")


#else子句：else區塊是可選的，它只在"區塊沒有發生任何異常try"時才會執行
try:
    result = 10 / 2
except ZeroDivisionError:
    print("除數不能為零！")
else:
    print(f"計算成功！結果是：{result}") # try 成功，此行會執行


#finally子句：finally區塊也是可選的，但它是無論是否異常，它一定會執行。(可用於"清理"功能)
try:
    f = open('myfile.txt', 'w')
    # 可能發生錯誤的寫入操作
    f.write("Hello, Python!")
    # print(10/0) # 取消註解此行來模擬異常
except IOError:
    print("檔案寫入錯誤！")
finally:
    f.close()
    print("清理工作：檔案已關閉。")


#try區塊中有多異常情形需被檢測
#1.也可多except區塊：
try:
    x = int(input("請輸入一個數字: "))
    result = 10 / x
except ValueError: #檢查輸入無效錯誤情況
    print("輸入無效，請輸入一個有效的數字。")
except ZeroDivisionError: #檢查為零的情況
    print("除數不能為零。")

#2.用一個except，並放置入元組：
try:
    # 可能引發 ValueError 或 TypeError 的程式碼
    x = int("abc") + "xyz"
except (ValueError, TypeError) as e:
    print(f"發生了數值或類型錯誤: {e}")
#也可"except Exception as e:" 可以捕捉幾乎所有標準異常，並將異常物件賦值給變數e
try:
    # 可能引發 ValueError 或 TypeError 的程式碼
    x = int("abc") + "xyz"
except Exception as e:
    print(f"發生了數值或類型錯誤: {e}")


#raise
#1.主動引發異常(raise)：用來驗證函式或要刻意紀錄時等功能使用
def set_age(age):
    if age < 0:
        raise ValueError("年齡不能為負數。")
    print(f"年齡已設定為: {age}")

try:
    set_age(-5)
except ValueError as e:
    print(f"錯誤: {e}")

#2.重新引發異常：except區塊中，可用不帶任何參數的raise來重新引發剛剛的異常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("記錄錯誤到日誌：發生除零錯誤。")
    raise # 將異常重新拋出


#自訂義異常：
#自定義 AgeException：用class分類
class AgeException(Exception):
    """用於處理無效年齡的自定義異常"""
    def __init__(self, message):
        super().__init__(message)

def enter_age(age):
    if age < 0:
        raise AgeException("年齡必須是正整數。")
    if age % 2 == 0:
        print("年齡是偶數。")
    else:
        print("年齡是奇數。")

try:
    num = int(input("請輸入您的年齡: "))
    enter_age(num)
except ValueError:
    print("請輸入一個數字。")
except AgeException as e:
    print(f"自定義異常: {e}")

#------------------------------------------------------------------------------
#範例1：互動式計算機：撰寫一個程式，讓使用者輸入一個簡單的數學表達式（例如 10 + 5），計算並輸出結果。
#程式需要處理以下情況：
#輸入格式不正確（不是三個元素），引發自定義的 FormulaError。
#第一個和第三個元素不是數字，引發 ValueError 並轉換為 FormulaError。
#運算子不是 + 或 -，引發 FormulaError。
#使用者輸入 quit 時結束程式
class FormulaError(Exception):
    """自定義公式錯誤異常"""
    pass

def parse_input(user_input):
    """解析使用者輸入並驗證格式"""
    input_list = user_input.split()
    if len(input_list) != 3:
        raise FormulaError("輸入格式錯誤，應為：數字 運算子 數字")
    
    n1_str, op, n2_str = input_list
    try:
        n1 = float(n1_str)
        n2 = float(n2_str)
    except ValueError:
        raise FormulaError("第一個和第三個值必須是數字")
        
    if op not in ('+', '-'):
        raise FormulaError(f"不支援的運算子: {op}")
        
    return n1, op, n2

def calculate(n1, op, n2):
    """執行計算"""
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2

while True:
    user_input = input("請輸入公式 (或輸入 'quit' 離開): ")
    if user_input.lower() == 'quit':
        break
    try:
       n1, op, n2 = parse_input(user_input)
       result = calculate(n1, op, n2)
       print(f"結果是: {result}")
    except FormulaError as e:
       print(f"錯誤: {e}")

#範例2：檔案內容寫入與清理：撰寫一個函式，接收檔案路徑和要寫入的文字。
#嘗試以寫入模式 ('w') 開啟檔案並寫入內容。
#使用 try-except 捕捉可能發生的 IOError（例如，如果檔案路徑是唯讀的目錄）。
#無論成功或失敗，都必須使用 finally 確保檔案被正確關閉
def write_to_file(path, text):
    f = None # 先初始化變數
    try:
        f = open(path, 'w', encoding='utf-8')
        f.write(text)
        print(f"成功寫入內容到 '{path}'")
    except IOError as e:
        print(f"檔案寫入失敗: {e}")
    finally:
        if f: # 確保檔案物件成功建立才關閉
            f.close()
            print(f"檔案 '{path}' 已關閉。")
#測試
write_to_file("test.txt", "這是異常處理的練習。")
# 嘗試寫入一個無效路徑 (在多數系統上會失敗)
write_to_file("non_existent_dir/test.txt", "這段文字不會被寫入。")
