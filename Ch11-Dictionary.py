#建立字典：建立字典主要有兩種方式：使用大括號 {} 或使用 dict() 建構函式。
# 方法一：使用大括號
my_dict1 = {"name": "Alice", "age": 25}
print(my_dict1)

# 方法二：使用 dict() 建構函式
my_dict2 = dict(name="Bob", age=30)
print(my_dict2)

# 建立一個空字典
empty_dict = {}
print(empty_dict)

#------------------------------------------------------------------------------

#查詢與存取 (Querying and Accessing)
#中括號 []：如果指定的鍵不存在，Python 會引發 KeyError 錯誤
#get()：這是一種更安全的方式。如果鍵不存在，它會返回 None（或您指定的預設值），而不會引發錯誤 。

student_scores = {"Alice": 95, "Bob": 88}
print(student_scores["Alice"])
print(student_scores[1]) #輸出keyerroe錯誤
print(student_scores.get("Alice"))
print(student_scores.get(1)) #輸出none

#------------------------------------------------------------------------------

#新增與更新 (Adding and Updating)：字典是"可變"的。
#中括號[]：如果"鍵"已存在，此操作會「更新」其對應的值；如果鍵不存在，則會「新增」一個新的鍵值對。
#update()：用於合併另一個字典或可迭代的鍵值對。如果鍵重複，後者會覆蓋前者。
student_scores = {"Alice": 95, "Bob": 88}
student_scores["Alice"]=80
print(student_scores)
student_scores["Cabrera"]=100

new_scores = {"Alice": 95,"David": 87}
student_scores.update(new_scores)
print(student_scores)

#------------------------------------------------------------------------------

#刪除 (Deleting)
#del 關鍵字：刪除指定的鍵值對。如果鍵不存在，會引發 KeyError6
#pop()：刪除指定鍵的鍵值對，並返回其值。這在需要使用被刪除的值時非常有用
#clear() 方法：清空字典中的所有鍵值對，使其成為一個空字典

student_scores = {'Alice': 98, 'Bob': 90, 'David': 85}
del student_scores["Bob"]
print(student_scores)
bobscores=student_scores.pop("Bob")
print(bobscores)
print(student_scores)

student_scores.clear()
print(student_scores)

#------------------------------------------------------------------------------

#排序 (Sorting)：雖然字典本身(Python3.7起)保持插入順序，但我們經常需要根據鍵或值對其進行排序。
#排序通常是透過sorted()函式完成的，它會返回一個新的排序後的"列表"，而不會修改原始字典。
#按鍵Key排序：
student_scores = {"Charlie": 92, "Alice": 95, "Bob": 88}
sortedsc=sorted(student_scores)
print(sortedsc) #僅列出"key"串列
sorted_items_by_key = sorted(student_scores.items()) #需要列出值，加上items()函數
print(sorted_items_by_key)
sorted_items_by_key = sorted(student_scores.items(),reverse=True)
print(sorted_items_by_key)

#按值Value排序：這需要使用 lambda 函式來指定排序的依據
student_scores = {"Charlie": 92, "Alice": 95, "Bob": 88}

sortedsc=sorted(student_scores, key=lambda i:i[0]) #用"key"排列
print(sortedsc)

sortedsc=sorted(student_scores.items(),key=lambda items:items[1],reverse=True)
print(sortedsc)
#用"value"來進行排序→items()；由小到大故要降冪排列→reverse=True

#------------------------------------------------------------------------------

#練習一：計數器應用
#題目：統計一個串列中每個單字出現的次數。

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts={}
firstword=words[0]
for word in words[:]:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)

#使用 get(key, 0) 的技巧，如果word不存在，返回0並加1；若存在，返回其當前計數並加 1
#如果 word 已存在，就取出它的值並加 1。
#如果 word 不存在，就從 0 開始加 1。
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

#------------------------------------------------------------------------------

#練習二：資料分組 p02
#題目：將一個包含學生姓名和分數的元組列表，按分數是否及格（>=60）進行分組。

students = [('Alice', 85), ('Bob', 55), ('Charlie', 95), ('David', 40)]
grouped_students = {'pass': [], 'fail': []}

for name,score in students:
    if score >= 60 :
        grouped_students['pass'].append(name)
    else:
        grouped_students['fail'].append(name)
print(grouped_students)

#------------------------------------------------------------------------------

#練習三：巢狀字典操作 p03
#題目：給定一個巢狀字典，更新'Bob'的數學成績為95，並新增'David'的資料。數學成績為78,英文成績為:82
student_grades = {
    'Alice': {'math': 90, 'english': 85},
    'Bob': {'math': 88, 'english': 92}
}

student_grades["Bob"]["math"]=95
davidinfo={"David":{"math":78,"english":82}}
student_grades.update(davidinfo)
print(student_grades)

#------------------------------------------------------------------------------

#題目1：建立一個字典，包含你的姓名、年齡和城市，並將其印出

mydict=dict(name="ben",age=26,city="tao")
print(mydict)

#------------------------------------------------------------------------------

#題目2：在上述字典中，新增一個鍵值對，"occupation": "Teacher"
mydict["occupation"]="teacher"
print(mydict)

#------------------------------------------------------------------------------

#題目3：修改上述字典中的年齡為 41
mydict["age"]=41
print(mydict)

#------------------------------------------------------------------------------

#題目4：從字典中刪除 city 這個鍵值對。w04 詳解：
del mydict["city"]
print(mydict)

#------------------------------------------------------------------------------

#題目5：給定字典 {"apple": 3, "banana": 5, "orange": 2}，計算所有水果的總數。
fruits = {"apple": 3, "banana": 5, "orange": 2}
total_fruits = sum(fruits.values())
print(f"水果總數為: {total_fruits}") # 輸出: 水果總數為: 10

#------------------------------------------------------------------------------

#題目6：遍歷字典 fruits，並以 "水果: [名稱], 數量: [數量]" 的格式印出每一項。 w06 詳解：
fruits = {"apple": 3, "banana": 5, "orange": 2}
for fruit, count in fruits.items():
    print(f"水果: {fruit}, 數量: {count}")

#------------------------------------------------------------------------------

#題目7：找出 fruits 字典中數量最多的水果名稱。 w07 詳解：
fruits = {"apple": 3, "banana": 5, "orange": 2}
# max 函式的 key 參數可以接收一個函式，這裡用 fruits.get 來告訴 max 函式比較字典的值
most_abundant_fruit = max(fruits, key=fruits.get)
print(f"數量最多的水果是: {most_abundant_fruit}") # 輸出: 數量最多的水果是: banana

#------------------------------------------------------------------------------

#題目8：將兩個字典 dict1 = {'a': 1, 'b': 2} 和 dict2 = {'b': 3, 'c': 4} 合併成一個新字典。 詳解：
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# 使用字典解包 (unpacking) 的方式，這是 Python 3.5+ 的現代語法
merged_dict = {**dict1, **dict2}
print(merged_dict) # 輸出: {'a': 1, 'b': 3, 'c': 4}
# 注意：重複的鍵 'b'，其值被後面的 dict2 覆蓋

#------------------------------------------------------------------------------

#題目9：建立一個字典，其鍵為 1 到 5 的數字，值為該數字的平方。 詳解：
# 使用字典推導式 (Dictionary Comprehension)
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict) # 輸出: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#------------------------------------------------------------------------------

#題目10：反轉一個字典的鍵和值。假設字典中的值都是唯一且不可變的
original_dict = {"name": "Alice", "id": "A01"}
reversed_dict = {value: key for key, value in original_dict.items()}

print(reversed_dict)

#------------------------------------------------------------------------------

#字典生成式
reversed_dict = {}
for key, value in original_dict.items():
    reversed_dict[value] = key
#變為
reversed_dict = {value: key for key, value in original_dict.items()}
