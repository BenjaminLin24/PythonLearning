empty_tuple = ()
print(f"空元組: {empty_tuple}, 型態: {type(empty_tuple)}")

# 2. 建立包含多個元素的元組
mixed_tuple = (10, "hello", 3.14)
print(f"混合型態元組: {mixed_tuple}")

# 3. 建立巢狀元組 (Nested Tuple)
nested_tuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(f"巢狀元組: {nested_tuple}")

# 4. 建立只有一個元素的元組，必須在元素後加上逗號
single_element_tuple = (50,) # 若寫成 (50)，會被視為整數 int
print(f"單一元素元組: {single_element_tuple}, 型態: {type(single_element_tuple)}")

# 5. 省略括號的元組打包 (Tuple Packing)
packed_tuple = 1, 2, 'a' # Python 會自動將其打包成元組
print(f"打包元組: {packed_tuple}, 型態: {type(packed_tuple)}")

#------------------------------------------------------------------------------

#查詢 (Querying/Accessing)
#索引 (Indexing): 使用方括號 [] 和索引值來存取特定位置的元素，索引從 0 開始。
#切片 (Slicing): 使用 [start:end:step] 來提取一部分元素，形成一個新的元組。
#count() 方法: 計算元組中某個特定元素出現的次數。
#index() 方法: 找出某個元素在元組中首次出現的索引值，如果元素不存在會引發 ValueError。
#內建函式:
#len(): 獲取元組的長度（元素個數）。
#max(): 返回元組中的最大值（元素需為可比較型態）。
#min(): 返回元組中的最小值（元素需為可比較型態）。
my_tuple = ('p', 'y', 't', 'h', 'o', 'n', 'p', 'y')

# 索引
print(f"第一個元素: {my_tuple[0]}") # 輸出: p
print(f"最後一個元素: {my_tuple[-1]}") # 輸出: y

# 切片
print(f"從索引 1 到 4 的元素: {my_tuple[1:4]}") # 輸出: ('y', 't', 'h')
print(f"從頭到尾每隔一個元素取值: {my_tuple[::2]}") # 輸出: ('p', 't', 'o', 'p')
print(my_tuple[::-1]) #同樣可以翻轉元組的序列
# 方法
print(f"元素 'p' 出現的次數: {my_tuple.count('p')}") # 輸出: 2
print(f"元素 'h' 的索引值: {my_tuple.index('h')}") # 輸出: 3

# 內建函式
print(f"元組長度: {len(my_tuple)}") # 輸出: 8
numeric_tuple = (10, 5, 25, 15)
print(f"最大值: {max(numeric_tuple)}") # 輸出: 25
print(f"最小值: {min(numeric_tuple)}") # 輸出: 5

#練習：存取巢狀元組的元素
#從 aTuple = ("Orange", [10, 20, 30], (5, 15, 25)) 中取出數值 20。
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
bTuple = aTuple[1]
print(aTuple[1])
cTuple = bTuple[1]
print(cTuple)

#更簡潔之寫法：巢狀寫法
print(aTuple[1][1])

#------------------------------------------------------------------------------

#新增 (Adding)：不可變性，無法直接在現有的元組上新增元素，用「串接」來建一個新元組。
#使用 + 運算子: 將兩個元組合併成一個新的元組。
#轉換為串列(list): 轉換為串列，再用append()或extend()方法新增元素，再轉換回元組。

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 方法一：使用 + 運算子串接
new_tuple = tuple1 + tuple2
print(f"串接後的新元組: {new_tuple}") # 輸出: (1, 2, 3, 4, 5, 6)

# 也可以新增單一元素的元組
add_one_tuple = tuple1 + (99,)
print(f"新增單一元素後: {add_one_tuple}") # 輸出: (1, 2, 3, 99)

# 方法二：轉換為列表再轉回
temp_list = list(tuple1)
temp_list.append(99)
result_tuple = tuple(temp_list)
print(f"透過列表新增後: {result_tuple}") # 輸出: (1, 2, 3, 99)

#練習：合併兩個元組並移除重複項p
#給定tup1 = (1, 2, 3) 和 tup2 = (3, 4, 5)，合併它們並移除重複的元素 3。

tup1=(1,2,3)
tup2=(3,4,5)

list1=list(tup1)
list2=list(tup2)

del list2[0]

newlist=list1+list2
newtup=tuple(newlist)
print(newtup)

merged_tuple = tuple(set(tup1 + tup2)) #set為集合的功能，自動將重複物件刪除
print(f"合併並去重後的元組: {merged_tuple}") # 輸出可能是 (1, 2, 3, 4, 5) 或其他順序，因為集合是無序的

#------------------------------------------------------------------------------

#刪除 (Deleting)
#使用切片:切片組合，可以創建一個不包含特定元素的新元組，達到「間接刪除」的效果。
#del 關鍵字:del無法刪除元組中的單一元素，但可用來刪除整個元組變數在記憶體中的參考。
#轉換為列表:可以將元組轉為列表，使用 remove() 或 pop() 刪除元素後，再轉回元組。

my_tuple = (11, 22, 33, 44, 55)

# 方法一：使用切片間接刪除元素 (例如刪除 33)
# 組合索引為 2 之前和索引為 3 之後的部分
new_tuple = my_tuple[:2] + my_tuple[3:]
print(f"刪除 '33' 後的新元組: {new_tuple}") # 輸出: (11, 22, 44, 55)

# 方法二：轉換為列表再轉回
temp_list = list(my_tuple)
temp_list.remove(33) # 刪除第一個匹配的 33
result_tuple = tuple(temp_list)
print(f"透過列表刪除後: {result_tuple}") # 輸出: (11, 22, 44, 55)

# 方法三：使用 del 刪除整個元組
deletable_tuple = (1, 2, 3)
print(f"刪除前的元組: {deletable_tuple}")
del deletable_tuple
# print(deletable_tuple) # 這行會引發 NameError，因為變數已被刪除

#練習：刪除元組中所有指定的元素
#從元組 t = (1, 5, 2, 5, 3, 5) 中移除所有的 5。

t = (1, 5, 2, 5, 3, 5)

l=list(t)
print(l)

result=[i for i in l if i != 5]

newt=tuple(result)
print(newt)

#------------------------------------------------------------------------------

#排序 (Sorting)：元組沒有sort()方法，因為會改變元素的順序，違反特性。
#sorted():函式可以接受任何可疊代的物件，並返回一個新的已排序"列表"，而原始元組不變。
#key參數:在對複雜結構（如元組列表）進行排序時。我們可以提供一個函式（通常是lambda）來指定依據。

numeric_tuple = (66, 4, 17, 4)
string_tuple = ('apple', 'Orange', 'banana') # 注意大寫 O 會影響排序

# 對數字元組排序
sorted_list_num = sorted(numeric_tuple)
print(f"數字元組排序後的列表: {sorted_list_num}") # 輸出: [4, 4, 17, 66]

# 對字串元組排序 (預設依字母順序，大寫優先)
sorted_list_str = sorted(string_tuple)
print(f"字串元組排序後的列表: {sorted_list_str}") # 輸出: ['Orange', 'apple', 'banana']

# 忽略大小寫排序
sorted_list_case_insensitive = sorted(string_tuple, key=str.lower)
print(f"忽略大小寫排序後的列表: {sorted_list_case_insensitive}") # 輸出: ['apple', 'banana', 'Orange']

# 降序排序
sorted_list_desc = sorted(numeric_tuple, reverse=True)
print(f"降序排序後的列表: {sorted_list_desc}") # 輸出: [66, 17, 4, 4]

#練習：對元組列表依據第二個元素排序
#給定一個元組列表data = [('Alice', 92), ('Bob', 85), ('Charlie', 95)]，
#請根據學生的分數（第二個元素）進行升序排序。
data = [('Alice', 92), ('Bob', 85), ('Charlie', 95)]

sortdata = sorted(data, key=lambda x:x[1])
print(sortdata)

#lambda函數用於臨時定義(不同於def)，故在此時為定義x值為第二個，所以是x[1]

#------------------------------------------------------------------------------

#lambda函數：「 lambda 參數: 表達式 」

add = lambda x, y: x + y
print(add(3, 5))  # 輸出 8

#原型應要直接定義，用def來決定一個公式
def add(x,y):
    result=x+y
    return result
print(add(3, 5))

#------------------------------------------------------------------------------

#選擇10：注意字串和整數的不同
tup = ('30', '3', '2', '8')
print(sorted(tup)) #字串30為3開頭，故在8前

tup = (30,3,2,8)
print(sorted(tup)) #輸出2,3,8,30

#------------------------------------------------------------------------------

#題目1: 創建一個包含整數 10、字串 "hello" 和浮點數 3.14 的元組。
tup=(10,"hello",3.14)
print(tup)
print(type(tup))

#------------------------------------------------------------------------------

#題目2: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)，請取出第 4 到第 7 個元素。
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[3:7])

#------------------------------------------------------------------------------

#題目3: 將tup1 = (1, 2, 3)和tup2 = ('a', 'b', 'c')兩個元組合併成一個新的元組。
tup1 = (1, 2, 3)
tup2 = ('a', 'b', 'c')
tup=tup1+tup2
print(tup)

#------------------------------------------------------------------------------

#題目4: 計算元組 t = (1, 2, 2, 3, 2, 4, 2) 中，數字 2 出現了幾次。
t = (1, 2, 2, 3, 2, 4, 2)
print(t.count(2))

#------------------------------------------------------------------------------

#題目5: 找出元組 t = (10, 20, 30, 40, 50) 中元素 40 的索引值。
t = (10, 20, 30, 40, 50)
print(t.index(40))

#------------------------------------------------------------------------------

#題目6: 將person = ("John", 25, "USA")的值解包 (unpack) 到 name, age, country 三個變數中。
person = ("John", 25, "USA")
name, age, country =person
print(person)
print(f"Name: {name}, Age: {age}, Country: {country}")
# 說明: 元組解包允許將元組中的元素快速賦值給多個變數，要求變數數量與元組元素數量相同
#解包（unpacking）就是把一個「可迭代的資料結構」（例如：元組、串列、集合、字典等）中的元素，
#依序指定給多個變數的過程。簡單說，就是把「一包資料」打開，分別塞給對應的變數。

#------------------------------------------------------------------------------

#題目7: 檢查元組 t = (45, 45, 45, 45) 中的所有元素是否都相同。
t = (45, 45, 45, 45)
first=t[0]
for i in t[:]:
    if i == first :
        print(True)
    else:
        print(False) #會印出很多個true

t = (45, 45, 45, 45)
result = all(i == t[0] for i in t) #all條件代表全部都要符合
print(result)  # 輸出 True

def check_all_same(t):
    if not t: # 處理空元組的情況(空元組也會是true)
        return True
    first_element = t[0]
    return all(i == first_element for i in t)

print(f"所有元素是否相同: {check_all_same(t)}")

#------------------------------------------------------------------------------

#題目8:scores = [('Math', 88), ('English', 95), ('Science', 90)]，請找出分數最高的科目與分數。
scores = [('Math', 88), ('English', 95), ('Science', 90)]
high=max(scores,key=lambda x:x[1])
print(high)

#------------------------------------------------------------------------------

#題目9: 遍歷元組 t = (10, 20, 30, 40, 50) 並印出每一個元素。 
t = (10, 20, 30, 40, 50)
for element in t:
    print(element)
    
#------------------------------------------------------------------------------

#題目10: 將一個 range 物件 range(1, 6) 轉換為一個元組
tup=range(1,6)
tupp=tuple(tup)
print(tupp)
