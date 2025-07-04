#新增元素：在串列中新增元素有多種方法。
#append(item):item加到最後。
#insert(index, item):item加到index位置。
#extend(iterable) 或 + 運算子:合併另一元素並生成新串列。

sports = ['Tennis', 'Basketball']
print(f"初始串列: {sports}")

# 使用 append() 新增元素
sports.append('Soccer')
print(f"使用 append() 新增 'Soccer': {sports}")

# 使用 insert() 在索引 1 的位置新增元素
sports.insert(1, 'Baseball')
print(f"在索引 1 使用 insert() 新增 'Baseball': {sports}")

# 使用 extend() 合併另一個串列
extra_sports = ['Swimming', 'Cycling']
sports.extend(extra_sports)
print(f"使用 extend() 合併 {extra_sports}: {sports}")

# 使用 + 運算子合併串列（會回傳一個新串列）
newList = sports + ['Archery']
print(f"使用 + 運算子產生新串列: {newList}")
print(f"原始串列 sports 未改變: {sports}")

#------------------------------------------------------------------------------

#刪除元素
#remove(item):刪除串列中第一個出現的指定元素。如果元素不存在會引發ValueError。
#pop(index=-1):移除並回傳指定位置的元素。如果未提供索引預設移除並回傳最後一個元素。
#del list[index]:根據索引刪除元素。del還可以刪除整個串列或一個切片。
#clear(): 清空串列中的所有元素。

my_list = [10, 200, 300, 30, 40, 50, 600]
print(f"初始串列: {my_list}")

my_list.remove(30)
print(my_list)

my_list1=my_list.pop()
print(my_list1)
print(my_list)#剩下的元素

del my_list[1]
print(my_list)

print(my_list.clear())

#------------------------------------------------------------------------------

#查詢與存取元素
#索引Indexing:方括號[]和位置。從0開始，也可用負數從尾部開始（-1代表最後一個）。
#切片Slicing:[start:stop:step] 。
#len(list):串列的長度（元素個數）。
#count(item):指定元素在串列中出現的次數。
#index(item):指定元素在串列中首次出現的索引。若不存在則引發ValueError。
#in 運算子: 檢查某個元素是否存在，回傳布林值 True 或 False。

data = [10, 20, 30, 40, 50, 30, 60]
print(f"初始串列: {data}")
print(data[2])
print(data[1:4])
print(data[1:5:2])
print(data.count(40))
print(data.index(50))
print(50 in data)
print(100 in data)
print(700 not in data)

#------------------------------------------------------------------------------

#排序與反轉
#sort():對原串列進行排序，預設為升序。可用reverse=True進行降序排序。不回傳值。
#sorted(iterable):它會回傳一個新的已排序串列，而不改變原始串列。
#reverse():將串列中的元素順序反轉。不回傳值。
#切片[::-1]:產生一個新的反轉後的串列副本，不改變原始串列。

numbers = [5, 2, 8, 1, 9]
print(f"原始串列: {numbers}")
numbers.sort()#原本list改變，注意是由小到大排列，而非反過來
print(numbers)
numbers.sort(reverse=True)
print(numbers)
new_numbers=sorted(numbers)#產生新list，保留原本的
print(new_numbers)
numbers.reverse()
print(numbers)
numbers2=numbers[::-1]
print(numbers2)

#------------------------------------------------------------------------------

#List Comprehension（串列生成式）：簡化語法融合，字串、過濾或轉化元素皆可用。
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
print(evens)
evens = [i for i in range(10) if i % 2 == 0]
print(evens)

text = "hello world"
no_spaces = [char for char in text if char != ' ']
print(no_spaces)

#------------------------------------------------------------------------------

#練習一：平方值串列
#給定一個數字串列，請產生一個新的串列，其中包含原串列中每個數字的平方值
numbers = [1, 2, 3, 4, 5, 6, 7]
new_numbers=[]
for i in numbers:
    new_numbers.append(i*i)
    print(new_numbers)

new_numbers=[(i*i) for i in numbers]#List Comprehension
print(new_numbers)

#------------------------------------------------------------------------------

#練習二：篩選長單字
#編寫名為get_long_words(input_list, min_len)的函式。
#接收一個字串串列和一個最小長度整數，回傳一個只包含長度大於或等於min_len的單字新串列
def get_long_words(input_list, min_len):
    list_to_return = []
    for word in input_list:
        if len(word) >= min_len:
            list_to_return.append(word)
    return list_to_return
# 測試函式
sample_words = ['bird', 'carpet', 'bicycle', 'orange', 'floccinaucinihilipilification']
min_length = 8
long_words = get_long_words(sample_words, min_length)
print(f"長度大於等於 {min_length} 的單字: {long_words}")


def get_long_words(input_list, min_len):
    return [word for word in input_list if len(word) >= min_len]

test=['abcd','efg','hijklmn','o','pq']
min_len = 5
long_word=get_long_words(test,min_len)
print(long_word)

#------------------------------------------------------------------------------

#練習三：尋找第二大數。給定一個數字串列，找出其中的第二大數[6]。
example=[8, 2, 15, 1, 9]

sorted_list = sorted(example, reverse=True)#法一，排序取第二個
second_largest = sorted_list[1]
print("第二大數是：", second_largest)

# 解法：先去重複數字，再排序
data = [8, 2, 15, 1, 9, 15] #(若有重複) 加入重複的 15
print(f"原始資料: {data}")

# 1. 使用 set 去除重複元素，再轉回 list
unique_data = list(set(data))
print(f"去除重複後: {unique_data}")

# 2. 對去重後的串列進行排序
unique_data.sort()
print(f"排序後: {unique_data}")

# 3. 檢查串列長度是否足夠，然後取出倒數第二個元素
if len(unique_data) >= 2:
    second_largest = unique_data[-2]
    print(f"第二大數是: {second_largest}")
else:
    print("串列中的獨立數字不足兩個，無法找到第二大數。")

#------------------------------------------------------------------------------

#選擇9
a = ['Learn', 'Quiz', 'Practice', 'Contribute']
b = a
c = a[:]#-----→雖然結果一樣是a，但不會影響原本的a；b會連動是因b與a記憶體位置相同
print(a)
print(b)
print(c)

b[0] = 'Code'
print(a)
print(b)
print(c)

c[1] = 'Mcq'
print(a)
print(b)
print(c)

#------------------------------------------------------------------------------

#第一題：計算並印出串列 [10, 20, 30, 40, 50] 中所有數字的總和與平均值
num=[10,20,30,40,50]
print(sum(num))
print(sum(num)/len(num))

#------------------------------------------------------------------------------

#第二題：將串列 [100, 200, 300, 400, 500] 反轉
num=[100,200,300,400,500]
new_num=num[::-1]
print(new_num)

num=[100,200,300,400,500]
num.reverse()
print(num)

#------------------------------------------------------------------------------

#第三題：找出串列 [8, 2, 15, 1, 9] 中的最大值與最小值
num=[8,2,15,1,9]
print(max(num),min(num))

#------------------------------------------------------------------------------

#第四題：'Football'在['Cricket','Football','Hockey','Football','Tennis']出現次數
sports=['Cricket','Football','Hockey','Football','Tennis']
football=sports.count("Football")
print(football)

#------------------------------------------------------------------------------

#第五題：將兩個串列 ['a', 'b', 'c'] 和 ['d', 'e', 'f'] 合併成一個新串列
a=['a', 'b', 'c']
d=['d', 'e', 'f']
ad=a+d
print(ad)

a.extend(d)
print(a)

#------------------------------------------------------------------------------

#第六題：移除串列 ['Red', 'Green', 'Blue', 'Green'] 中第一個 'Green'
num=['Red', 'Green', 'Blue', 'Green']
num.remove("Green")
print(num)

num.pop(1)
print(num)

del num[1]
print(num)

#------------------------------------------------------------------------------

#第七題：將串列 [3, 8, 1, 6, 0, 8, 4] 進行升序排序
num=[3,8,1,6,0,8,4]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

ascending=sorted(num)
descending=sorted(num,reverse=True)
print(ascending)
print(descending)

#------------------------------------------------------------------------------

#第八題：建立一個串列 [10, 20, 30] 的副本，並修改副本，驗證原始串列未被改變
num=[10,20,30]
new_num=sorted(num)
print(new_num)
new_num[0]=0
print(new_num)
print(num)

nnew_num=num.copy() #copy函數也可複製出新的且不改變原值
print(nnew_num)
nnew_num[0]=0
print(nnew_num)
print(num)

#------------------------------------------------------------------------------

#第九題：使用串列生成式，從 range(10) 中篩選出所有的偶數，產生一個新串列
even=[i for i in range(10) if i%2 ==0 ]
print(even)

#------------------------------------------------------------------------------

#第十題：將一個字串串列 ['hello', 'world'] 轉換為單一字串 'hello world'
words=['hello', 'world']
for i in words:
    new_list = str(i)
    print(new_list)
#迴圈方式不太正確
words = ['hello', 'world']
sentence = ''
for i in words:
    sentence += i + ' '
sentence = sentence.strip()  # 去掉最後多出來的空白
print(sentence)

#使用join函數，可將字串串起
string_list = ['hello', 'world']
result_string = " ".join(string_list)
print(result_string)
