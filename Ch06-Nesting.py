#第一題：寫一個程式，印出 1 到 50 之間所有 7 的倍數
for i in range(1,51):
    if i%7 == 0:
        print(i)
    
#--------------------------------------------------------------------

#第二題：計算一個巢狀串列中所有數字的總和。(https://realpython.com/nested-loops-python/)
data = [[1, 2, 3], [4, 5], [6,3,3]] 
total=0
for i in data: #先計算data串列中的每個小集合(1+2+3、4+5、6+3+3)
    for n in i: #再將每個集合計算總和(6+9+12)
        total += n
print(total)
    
#--------------------------------------------------------------------

#第三題：安全地建立一個 3x3 的零矩陣，使其每一列都是獨立的。

value=float(input("輸入任意數字"))
matrix= [[value for _ in range(3)] for _ in range(3)]
print(matrix)

matrix = [[0 for _ in range(3)] for _ in range(3)]
# 驗證
matrix[0][0] = 5
print(matrix)
    
#--------------------------------------------------------------------

#第四題：找出巢狀串列中的最大值。
data = [[1, 9, 2], [8, 3, 7], [4, 6, 5]]
mmax=data[0][0] #先設定初始值
for maxim in data:
    for i in maxim:
        if i >= mmax: #層層比較，若比到大的就會替換掉
            mmax = i
print(mmax)
   
#--------------------------------------------------------------------

#第五題：給定兩個串列，印出所有可能的元素配對。
list1 = ['a', 'b']
list2 = [1, 2]
for i in list1:
    for j in list2:
        print((i,j))
for i in list2:
    for j in list1:
        print(f"({i}, {j})")
  
#--------------------------------------------------------------------

#第六題：檢查一個密碼是否符合所有規則：長度至少8個字元、必須包含數字。
password=input("請輸入至少8個字元的密碼")
len_password=len(password)
is_word=any(char.isdigit() for char in password) #any函數：內有一個元素就是true
#isdigit()為檢測字串中是否全部為整數
if len_password >= 8 and is_word == True:
    print("輸入有效")
else:
    print("輸入無效")


password=input("請輸入至少8個字元的密碼")
is_valid = False
if len(password) >= 8:
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break # 找到數字就可跳出內層迴圈
    if has_digit:
        is_valid = True

if is_valid:
    print("密碼有效")
else:
    print("密碼無效")

#--------------------------------------------------------------------

#第七題：將一個巢狀串列「扁平化」成單一串列。
nested = [[1, 2], [3, 4, 5], [6]]
flat=[] #建立空串列給予增加
for i in nested:
    for j in i:
        flat.append(j) #以j來增加
print(flat)

#--------------------------------------------------------------------

#第八題：印出一個靠右對齊的數字金字塔（高度為 5）
for i in range(1, 6):
    # 先印空白（高度 - 目前行數）
    spaces = (5 - i) * " "
    print(spaces, end="")
    
    # 再印數字 1 到 i
    for j in range(1, i + 1):
        print(j, end="")
    
    # 換行
    print()

height = 5
for i in range(1, height + 1):
    # 先印空格
    for _ in range(height - i):
        print(" ", end="")
    # 再印數字
    for j in range(1, i + 1):
        print(j, end="")
    print()

#--------------------------------------------------------------------

#第九題：找出成績最高的學生
grades = {"小明": 88, "小華": 95, "小英": 92}
top_grade=0
top_student=""
for student,grade in grades.items():
#for student, grade in grades:
#這裡會只取得字典的「key」（學生名字），而不是 key 和 value。
#正確應該用 grades.items() 才會同時拿到學生和分數。
    if grade >= top_grade:
        top_grade = grade
        top_student=student
print(f"最高分學生：{top_student}，分數為{top_grade}")

#--------------------------------------------------------------------

#第十題：找出一個字串中，所有重複出現的字元。
input_str = "hello world"
duplicates = []

for i in range(len(input_str)): #用"第幾個字"來比
    for j in range(i + 1, len(input_str)): #比完一個字後再比下個字，不重複比較
        if input_str[i] == input_str[j] and input_str[i] not in duplicates and input_str[i] != ' ':
            duplicates.append(input_str[i])

print(f"重複的字元有: {duplicates}")