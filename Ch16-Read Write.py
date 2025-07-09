#打開檔案
#open()：用於檔案操作的核心內建函數。會回傳一個檔案物件（也稱為handle），後續的所有檔案操作都將透過這個物件進行。
#語法：open(file, mode='r', encoding=None)；主要參數：
#file：要開啟的檔案路徑（字串）。
#mode：一個字串，用以指定檔案的開啟模式，預設為 'r'（唯讀）。
#encoding：指定讀寫文字檔案時的編碼，如'utf-8'。在處理包含非ASCII字元的文字檔案時
#(明確指定編碼是個好習慣，可以避免 UnicodeDecodeError)

file = open("example.txt", "w")

#讀取檔案
#read(size)：一次性讀取整個檔案的內容（若未指定 size），並以單一字串形式回傳。對於非常大的檔案，這可能會消耗大量記憶體。
#readline()：每次讀取檔案中的一行，包含行尾的換行符 \n。當再次呼叫時，它會繼續讀取下一行。
#readlines()：讀取檔案的所有行，並將它們以字串列表的形式回傳，每一行是列表中的一個元素。
#迭代檔案物件：這是處理檔案最常用且最高效的方式，特別是對於大檔案。它逐行讀取檔案，不會一次將所有內容載入記憶體

content = file.read()  # 讀取整個檔案
line = file.readline()  # 讀取單行
lines = file.readlines()  # 讀取所有行到一個列表

#寫入檔案
#write(string)：將指定的字串寫入檔案。此方法不會自動在字串末尾添加換行符，需要手動加入 \n 。
#writelines(list_of_strings)：將一個包含多個字串的列表寫入檔案。同樣地，它也不會自動添加換行符

file.write("Hello, World!")
file.writelines(["Line 1\n", "Line 2\n"])

#關閉檔案
file.close()

#with語句：with open(...) as ...，推薦使用 with 語句來自動處理檔案的開啟和關閉

with open("example.txt", "r") as file:
    content = file.read()

#操作範例
file = open("example.txt", "w")
file.write("Hello, World!")
file.close() #用open就一定要有close，才會正確紀錄資料，避免關閉後都洗掉

file = open("example.txt", "r")
content = file.read()  # 讀取整個檔案
print(content)

with open("example.txt", "r") as file:
    content = file.read() #寫入資料
print(content)

lines_to_write = ["第一行文字。\n", "這是第二行。\n", "最後一行。\n"]
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("這是一個單獨寫入的句子。\n")
    f.writelines(lines_to_write)

with open('output.txt', 'rb') as f:
    # 讀取前 10 個位元組
    data = f.read(10)
    print(f"目前指標位置: {f.tell()}") # 輸出: 10
    
#測試用"w"寫入模式，成功創建新檔案
with open('config11.txt', 'w', encoding='utf-8') as f:
    f.write("test")
    
#------------------------------------------------------------------------------

#範例1: 過濾顯示檔案內容 讀取一個檔案，但只顯示不以 # 符號開頭的行
# 檔案 'config.txt' 內容:
# # 這是設定檔
# user = admin
# password = 12345
#
# # 資料庫設定
# db_host = localhost

with open('config.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip().startswith('#'):
            print(line, end='')

#------------------------------------------------------------------------------

#範例2：數字排序 從一個存放了若干數字的文字檔中讀取所有數字，排序後輸出
# 檔案 'numbers.txt' 內容:
# 15 8 99 42 4 23

numbers = []
with open('numbers.txt', 'r') as f:
    content = f.read()
    # split() 會將字串按空白分割成一個列表
    num_strings = content.split(",")
    for s in num_strings:
        numbers.append(int(s))

numbers.sort()
print("排序後的數字:", numbers) # 輸出: [4, 8, 15, 23, 42, 99]

#------------------------------------------------------------------------------

#範例3：字母凱撒加密：讀取一個英文文字檔，將字母進行位移加密（A→B,B→C,..,Z→A），並將結果寫入新檔案
#檔案 english.txt

new_content = ""
with open('english.txt', 'r') as f:
    content = f.read()
    for char in content:
        ascii_val = ord(char)
        if 'a' <= char <= 'z':
            new_char = chr((ascii_val - ord('a') + 1) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr((ascii_val - ord('A') + 1) % 26 + ord('A'))
        else:
            new_char = char
        new_content += new_char

with open('encrypted.txt', 'w') as f_out:
    f_out.write(new_content)
    
print("檔案加密完成！")

#此程式利用 ord() 函數取得字元的 ASCII 值，並利用 chr() 將 ASCII 值轉回字元。
#ASCII裡面大小寫有不同值，因此不能直接換。

#------------------------------------------------------------------------------

#練習1：讀取並印出檔案：編寫一個程式，讀取名為 learning.txt 的檔案，並將其內容完整地印在控制台上
try:
    with open("learning.txt","r",encoding="utf-8") as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print("檔案不存在")
    
#------------------------------------------------------------------------------

#練習2：寫入使用者輸入：提示使用者輸入五行文字，並將這五行文字寫入 output1.txt 檔案中，每行文字佔一行
with open("outpu1.txt","w",encoding="utf-8") as f:
    for i in range(5):
        line=input(f"請輸入第{i+1}行文字")
        f.write(line+"\n")
print("資料已成功寫入")

#------------------------------------------------------------------------------

#練習3：附加日誌：設計一個函式，每次呼叫時將目前的日期時間和一條訊息附加到 app.log 檔案中
import datetime

def callandwrite(message):
    with open("app.log","a",encoding="utf-8") as f:
        timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{message}+[{timestamp}]\n")

callandwrite("早安")
callandwrite("今天早上1662大塞車，坐公車兩小時") #關鍵是使用附加模式 'a'，確保每次的記錄都添加在檔案末尾

#------------------------------------------------------------------------------

#練習4：計算檔案行數：編寫一個程式，計算一個檔案中有多少行
try:
    with open('data.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)
        print(f"檔案總共有 {line_count} 行。")
except FileNotFoundError:
    print("檔案不存在。")
#readlines() 將檔案所有行讀入一個列表，列表的長度 len() 即為檔案的行數
#sum(1 for _ in f)：是 生成器表達式（generator expression），它實際上會在每一行中產生數字 1。
#然後，sum() 函式會將這些 1 累加起來，從而得出檔案的行數。
try:
    with open('data.csv', 'r', encoding='utf-8') as f:
        line_count = sum(1 for _ in f)  # 計算行數
        print(f"檔案總共有 {line_count} 行。")
except FileNotFoundError:
    print("檔案不存在。")
    
#f.readlines() 會將整個檔案的內容讀入記憶體並返回一個列表，這樣會佔用更多的記憶體。
#sum(1 for _ in f) 是逐行處理檔案，不會一次性將整個檔案讀入記憶體，因此對於大型檔案會更高效。

#------------------------------------------------------------------------------

#練習5：大小寫轉換：讀取一個英文文字檔，將其中的大寫字母轉為小寫，小寫字母轉為大寫，並寫回原檔案
file_path = 'english_text.txt'
try:
    with open(file_path, 'r+', encoding='utf-8') as f:
        content = f.read()
        swapped_content = content.swapcase() # swapcase()：大小寫轉換"字串字母"，回傳一新字串
        f.seek(0) # 將指標移回開頭，因為要重新寫入作業
        f.truncate() # 用來清空檔案中的現有內容。如果不清空，寫入的內容會覆蓋舊的，但不會去除舊內容後的字元。
        f.write(swapped_content)
    print("大小寫轉換完成。")
except FileNotFoundError:
    print("檔案不存在。")
    
#------------------------------------------------------------------------------

#練習6：讀取一個檔案，第一次直接印出全部內容，第二次將所有行存入串列後再遍歷印出
with open ("poem.txt","r",encoding="utf-8") as f:
    content=f.read()
    print(content)
    
    f.seek(0) # 指標已在檔尾，需移回開頭才能再次讀取
    
    contents=f.readlines()
    for line in contents:
        print(line, end='') # 逐行印出，避免額外的換行符號

#f.readlines() 會返回一個串列，其中每一個元素都是檔案中的一行（包括每行的換行符 \n）。
#print(contents, end='') 會將整個串列 contents 以一個 字串的形式印出，類似 [ 'line1\n', 'line2\n',  ]

#------------------------------------------------------------------------------

#練習7：計算數字總和與平均值：讀取一個每行包含一個數字的檔案，計算所有數字的總和與平均值
total = 0
count = 0
try:
    with open('scores.txt', 'r') as f:
        for line in f:
            total += float(line.strip())
            count += 1
    average = total / count if count > 0 else 0
    print(f"總和: {total}, 平均值: {average:.2f}")
except (FileNotFoundError, ValueError):
    print("檔案不存在或內容格式錯誤。")

#------------------------------------------------------------------------------

#練習8：全域性取代：將檔案中所有出現的特定單字（'Python'）取代為另一個單字（'World'）。
file_path = 'document.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content.replace('Python', 'World') #replace功能，將一字串置換為其他字串

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("取代完成。")

#------------------------------------------------------------------------------

#練習9：從一個問題庫檔案中讀取問題與答案，隨機打亂順序，並產生多份獨一無二的測驗卷檔案與對應的答案卷檔案
import random

# 假設 questions.txt 格式為: 問題;答案
questions = []
with open('questions.txt', 'r', encoding='utf-8') as f:
    for line in f:
        questions.append(line.strip().split(';'))

for i in range(5): # 產生 5 份測驗卷
    random.shuffle(questions)
    with open(f'quiz_{i+1}.txt', 'w', encoding='utf-8') as qf, \
         open(f'answer_{i+1}.txt', 'w', encoding='utf-8') as af:
        
        for index, item in enumerate(questions):
            qf.write(f"{index+1}. {item[0]}\n")
            af.write(f"{index+1}. {item[1]}\n")  
print("5 份隨機測驗卷已產生。")


import random

# 讀取問題庫檔案，格式假設為 "問題|答案"
def load_questions(filename):
    questions = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            question, answer = line.strip().split('|')
            questions.append((question, answer))
    return questions

# 隨機打亂問題順序並生成測驗卷和答案卷
def generate_exam(questions, num_exams):
    for i in range(num_exams):
        # 隨機打亂問題順序
        random.shuffle(questions)
        
        # 產生測驗卷與答案卷檔案
        exam_filename = f"exam_{i+1}.txt"
        answer_filename = f"answer_{i+1}.txt"
        
        with open(exam_filename, 'w', encoding='utf-8') as exam_file, \
             open(answer_filename, 'w', encoding='utf-8') as answer_file:
            for idx, (question, answer) in enumerate(questions):
                # 輸出測驗卷（僅包含問題）
                exam_file.write(f"{idx + 1}. {question}\n")
                # 輸出答案卷（問題與答案）
                answer_file.write(f"{idx + 1}. {question} - {answer}\n")

        print(f"已產生測驗卷：{exam_filename}")
        print(f"已產生答案卷：{answer_filename}")

# 主程式
def main():
    # 問題庫檔案名稱
    question_bank_file = "question_bank.txt"
    
    # 讀取問題庫
    questions = load_questions(question_bank_file)
    
    # 設定需要產生的測驗卷數量
    num_exams = 5  # 這裡假設產生5份測驗卷
    
    # 產生測驗卷與答案卷
    generate_exam(questions, num_exams)

if __name__ == "__main__":
    main()

#main()：
#1設定問題庫檔案名稱，讀取問題庫。
#2設定需要產生的測驗卷數量（在這裡預設為 5）。
#3呼叫 generate_exam() 來生成多份測驗卷與對應答案。

#------------------------------------------------------------------------------

#練習10：模擬 tail -f 功能：編寫一個程式，持續監控一個檔案的末尾，並即時印出新增的內容，類似 Linux 的 tail -f 命令
import time

def follow(thefile):
    thefile.seek(0, 2) # 跳到檔案末尾
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # 若無新內容，稍作等待
            continue
        yield line

with open('server.log', 'r', encoding='utf-8') as logfile:
    for line in follow(logfile):
        print(line, end='')

#seek(0, 2) 將指標移至檔案末尾。
#迴圈中不斷嘗試 readline()，如果讀到空字串，表示已到檔尾且無新內容，此時暫停一小段時間再試。
#如果讀到新的一行，就透過 yield 將其回傳，這使得 follow 函式成為一個產生器。
#for line in follow(logfile):是無限迴圈(while True:)，程式不會主動離開with區，也就不會關閉，除非手動中止。
#或：使用 Ctrl+C 中斷程式
#或：加入條件中止機制（例如偵測到某個關鍵字或時間限制）