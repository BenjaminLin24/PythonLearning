#讀取檔案並過濾註解行：讀取一個文字檔，並僅顯示非 # 開頭的行
try:
    with open('students.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # 移除行首尾的空白字元並檢查是否以 '#' 開頭
            if not line.strip().startswith('#'):
                print(line, end='')
except FileNotFoundError:
    print("錯誤：找不到指定的檔案。")

#讀取 CSV 並轉換為字典列表：
import csv

try:
    with open('sales.csv', mode='r', encoding='utf-8', newline='') as f:
        # 使用 DictReader，它會自動將第一行作為標頭
        reader = csv.DictReader(f)
        
        sales_data = []
        for row in reader:
            sales_data.append(row)
            # 可以像操作字典一樣存取資料
            print(f"產品: {row['product']}, 地區: {row['region']}, 銷售額: {row['sales']}")
    
    # sales_data 現在是一個字典列表
    # [{'product': 'Apple', 'region': 'North', 'sales': '1500'}, ...]
    
except FileNotFoundError:
    print("錯誤：找不到 sales.csv 檔案。")
    
#csv.DictReader讀取CSV檔案，比csv.reader更具可讀性，因為可以透過欄位名稱存取資料


#計算特定產品的總銷售額：基於上述範例，進一步處理sales_data列表，計算出 'Apple' 這個產品在所有地區的總銷售額。
#這需要將銷售額從字串轉換為數字進行加總

import csv
apple_total_sales=0
try:
    with open('sales.csv', mode='r', encoding='utf-8', newline='') as f:
        # 使用 DictReader，它會自動將第一行作為標頭
        reader = csv.DictReader(f)
        
        sales_data = []
        for row in reader:
            sales_data.append(row)
            if row['product'] == 'Apple':
                apple_total_sales += int(row['sales'])
            # 可以像操作字典一樣存取資料
            print(f"產品: {row['product']}, 地區: {row['region']}, 銷售額: {row['sales']}")
    print(f"總銷售額 : {apple_total_sales}")
    
    # sales_data 現在是一個字典列表
    # [{'product': 'Apple', 'region': 'North', 'sales': '1500'}, ...]
    
except FileNotFoundError:
    print("錯誤：找不到 sales.csv 檔案。")

#------------------------------------------------------------------------------

#json讀取寫入
#json.load(fp): 從檔案物件 fp 讀取 JSON 資料並反序列化為 Python 物件。
#json.loads(s): 從字串 s 讀取 JSON 資料並反序列化為 Python 物件。
#json.dump(obj, fp): 將 Python 物件 obj 序列化為 JSON 格式並寫入檔案物件fp。
#json.dumps(obj): 將 Python 物件 obj 序列化為 JSON 格式的字串。

#建立 Python 字典並存為 JSON 檔案：
import json
# 建立一個複雜的 Python 字典
quiz_data = {
    "title": "Python 檔案處理測驗",
    "questions": [
        {
            "id": 1,
            "text": "哪種模式用於附加寫入檔案？",
            "options": ["r", "w", "a", "x"],
            "answer": "a"
        },
        {
            "id": 2,
            "text": "哪個函式用於將 Python 物件寫入 JSON 檔案？",
            "options": ["load", "dump", "loads", "dumps"],
            "answer": "dump"
        }
    ]
}

# 將字典寫入 JSON 檔案
with open('quiz.json', 'w', encoding='utf-8') as f:
    # indent=4 讓 JSON 檔案有漂亮的縮排
    json.dump(quiz_data, f, ensure_ascii=False, indent=4)
#ensure_ascii=True(預設)：將ASCII轉換為Unicode；False則會保留中文等非ASCII字符
print("quiz.json 檔案已成功建立。")

#------------------------------------------------------------------------------

#練習1：編寫一個 Python 程式，讀取名為 poem.txt 的檔案，並將其內容完整印出到控制台。
try:
    with open ("poem.txt","r",encoding="utf-8") as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print("檔案 'poem.txt' 不存在。")
    
#------------------------------------------------------------------------------

#練習2：提示使用者輸入一行文字，並將該文字附加到 log.txt 檔案的末尾。每次執行程式，都應新增一行。
add=input("請輸入一行新文字")
with open ("log.txt","a",encoding="utf-8") as f:
    f.write(add+'\n')
print("寫入成功")

#------------------------------------------------------------------------------

#練習3：計算檔案行數，編寫一個函式 count_lines(filepath)，接收一個檔案路徑，回傳該檔案的總行數
def count_lines(filepath):
    try:
        with open (filepath,"r",encoding="utf-8") as f:
            lines=f.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0

num = count_lines('students.txt')
print(f"檔案共有 {num} 行。")
    
#------------------------------------------------------------------------------

#練習4：讀取 CSV 特定欄位，內容如下。請讀取檔案並只印出所有產品的名稱（ProductName 欄位）
import csv
try:
    with open('products.csv', 'r', encoding='utf-8', newline='') as f:
        reader=csv.DictReader(f)
        print("所有產品名稱")
        for row in reader:
            print(row['ProductName'])
except FileNotFoundError:
    print("檔案 'products.csv' 不存在。")

#------------------------------------------------------------------------------

#練習5：寫入列表到CSV，有一包含多字典的串列data，將其寫入名為output.csv的檔案中，包含標頭。
data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

import csv

headname=data[0].keys() #標題為第一組字典中的鍵key

with open ("output.csv","w",encoding="utf-8") as f:
    writer=csv.DictWriter(f, fieldnames=headname)
    writer.writeheader()  # 寫入標頭
    writer.writerows(data) # 寫入所有資料
print("資料已寫入 output.csv")

#------------------------------------------------------------------------------

#練習6：讀取 JSON 檔案，範例實作 3 中建立的 quiz.json 檔案，並印出測驗的標題 (title)
import json

try:
    with open('quiz.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"測驗標題: {data['title']}") #data為一字典，抓取其key
        print(data)
except FileNotFoundError:
    print("檔案 'quiz.json' 不存在。")
    
#------------------------------------------------------------------------------

#練習7：從 CSV 轉換到 JSON，第4題的products.csv，將其內容轉換為JSON，並存入 products.json
import csv
import json
data_list = []
try:
    with open('products.csv', 'r', encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file) #變成字典
        for row in reader: #字典行列建置
            data_list.append(row)
    
    with open('products.json', 'w', encoding='utf-8') as json_file:
        writer=json.dump(data_list,json_file, indent=4, ensure_ascii=False)
    
    print("成功轉換json")

except FileNotFoundError:
    print("找不到products.csv")
#先用csv.DictReader 將 CSV 讀取為字典列表，然後再使用 json.dump

#------------------------------------------------------------------------------

#練習8：處理數字排序
#題目：一個文字檔numbers2.txt 中包含多行數字，每行一個。讀取所有數字，將其排序後，印出到控制台

newlist=[]
try:
    with open ("numbers2.txt","r",encoding="utf-8") as f:
        for line in f:
            # 轉換為整數並加入列表
            newlist.append(int(line.strip()))
            
        newlist.sort()
        print("排序後的數字：")
        for num in newlist:
            print(num)
except FileNotFoundError:
    print("檔案 'numbers2.txt' 不存在。")
except ValueError:
    print("檔案中包含非數字內容。")

#讀取每一行後，需使用 int() 將字串轉換為整數才能進行數值排序。
#line.strip() 用於移除可能存在的空白或換行符

#------------------------------------------------------------------------------

#練習9：讀取一個英文檔english.txt，將每個字母進行凱薩加密（A->B,B->C,..,Z->A），並寫入新檔案encrypted.txt
def caesar_cipher(text): #先搞函式
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            result += char
    return result

try:
    with open("english.txt",'r',encoding="utf-8") as f_in:
        content = f_in.read()
        
    encrypted_content = caesar_cipher(content)
    
    with open("encrypted.txt",'w',encoding="utf-8") as f_out:
        f_out.write(encrypted_content)
    
    print("加密完成")
except FileNotFoundError:
    print("檔案 'english.txt' 不存在。")

#------------------------------------------------------------------------------

#練習10：安全的檔案附加函式，編寫一個函式 append_to_file(filename, text)，該函式接收檔名和字串。
#如果檔案存在，則將字串附加到末尾；如果不存在，則建立檔案並寫入字串。函式需能處理可能的 IOError。
def append_to_file(filename, text):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        print(f"成功將內容附加到 {filename}")
    except IOError as e:
        print(f"寫入檔案時發生錯誤: {e}")

# 使用範例
append_to_file('my_notes.txt', '這是第一條筆記。')
append_to_file('my_notes.txt', '這是第二條筆記。')