#全域變數 (Global Variable)
#定義: 在所有函式的「外部」，也就是程式的主體層級定義的變數。
#特性: 它的作用域涵蓋整個程式檔案，因此可以從任何函式內部或外部被存取。

message = "這是一個全域變數" # 在函式外定義

def print_message():
    print("在函式內存取:", message)

print_message()
print("在函式外存取:", message)


#區域變數 (Local Variable)
#定義: 在「函式內部」定義的變數。
#特性: 其作用域僅限於定義的函式內。函式執行完畢，變數就會被"銷毀"，無法從外部存取。

def create_local_variable():
    local_msg = "這是一個區域變數" # 在函式內定義
    print(local_msg)

create_local_variable()
# 下一行會產生 NameError，因為 local_msg 在函式外部是不可見的
# print(local_msg)


#LEGB 規則：Python 的變數查找順序
#L (Local): 首先在最內層的區域作用域 (函式內部) 尋找。
#E (Enclosing): 如果在區域找不到，則向外尋找上一層的函式作用域 (針對巢狀函式)。
#G (Global): 如果還是找不到，就到全域作用域尋找。
#B (Built-in): 如果全域找不到就會查Python內建的名稱空間(例如print,len等函式)。再找不到，就會引發NameError錯誤。

#區域變數的優先權 (遮蔽效應)：當區域變數與全域變數同名時，函式內部優先使用區域變數，這稱為「遮蔽 (Shadowing)」。

x = 10  # 全域變數

def function_scope_test():
    x = 99  # 區域變數，與全域變數同名
    print(f"函式內部印出的 x 是: {x}") # 會印出 99

function_scope_test()
print(f"函式外部印出的 x 仍然是: {x}") # 會印出 10


#在函式中修改全域變數：global 關鍵字，若想再函式內使用全域變數，就要加上global 變數
#若在函式中沒有先宣告區域變數，又直接打全域變數就會錯誤，若有再次打一個區域變數，即便與全域不同也可以運作

#錯誤的嘗試 (導致 UnboundLocalError) 
count = 0

def increment():
    # Python 看到下一行的賦值運算(+=)，會將 count 視為一個新的區域變數
    # 但在賦值前就試圖讀取它，因此會報錯
    print("嘗試讀取:", count) # 這行會引發 UnboundLocalError
    #count += 1

# increment() # 若取消註解，將會引發錯誤

#函式內有對變數「賦值」行為 (如 =、+=)，就會預設該變數為區域變數。
#因此，print(count) 試圖存取一個尚未被賦值的「區域變數」count，從而導致錯誤。

score = 100 # 全域變數

def update_score():
    global score  # 聲明此處要使用的是全域變數 score
    print(f"修改前，全域 score 為: {score}")
    score = score + 50 # 修改全域變數的值
    print(f"修改後，全域 score 為: {score}")

update_score()
print(f"函式執行完畢後，全域 score 變為: {score}")

#巢狀函式與nonlocal關鍵字：當函式中包著另一"巢狀"函式，並修改外部函式變數「非全域變數」，則需使用nonlocal。

def outer_function(): #2
    level = "外部函式變數" #3

    def inner_function(): #6
        nonlocal level  # 聲明 level 是來自於上一層(Enclosing)作用域的變數
        level = "由內部函式修改"
        print(f"在內部函式中: {level}") #7

    print(f"呼叫內部函式前: {level}") #4
    inner_function() #5
    print(f"呼叫內部函式後: {level}") #8

outer_function() #1


#可變型別(Mutable Types)陷阱：全域變數是可變型別(如串列list、字典dict)，在函式內可以修改「內容」而不用global
#但要「重新賦值」整個變數，則仍需global。

global_list = [10, 20, 30]

def modify_mutable_type():
    # 修改串列的內容，這是允許的，因為操作的是物件本身
    global_list.append(40)
    
    # 若執行下面這行，會建立一個新的「區域變數」global_list
    # global_list = [1, 2, 3] 

modify_mutable_type()
print(f"修改後的串列: {global_list}") # 輸出: [10, 20, 30, 40]

#產生新變數，用global關鍵字：
global_list = [10, 20, 30]

def modify_mutable_type():   
    global global_list
    # 若執行下面這行，會建立一個新的「區域變數」global_list
    global_list = [1, 2, 3] 

modify_mutable_type()
print(f"修改後的串列: {global_list}")


#全域變數過度使用會導致不易讀、混亂之類的問題，故能不用就不會一直用，用RETURN來定義更安全
# 不推薦的作法
player_health = 100
def take_damage_global(damage):
    global player_health
    player_health -= damage

# 推薦的作法
def take_damage_local(current_health, damage):
    return current_health - damage

player_health = 100
player_health = take_damage_local(player_health, 20)

#類別Class管理狀態:需要"共享"多個相關狀態的場景，將這些狀態封裝在一個類別中是更好的選擇。
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} 受到 {damage} 點傷害，剩餘生命: {self.health}")

p1 = Player("英雄", 100)
p1.take_damage(30)

#------------------------------------------------------------------------------

#練習7&8
data1 = {'a': 1}
def update_data():
    data1['b'] = 2

update_data()
print(data1)
#data1=[]，字典的新增規則，新增一組key-value，故為新增非修改，不違反原則，正常印出

data2 = {'a': 1}
def update_data():
    data2 = {'c': 3}

update_data()
print(data2)
#data2={}，字典的「更改」，意即重新賦值，重新賦值就要用global，修改為→
data2 = {'a': 1}
def update_data():
    global data2
    data2 = {'c': 3}

update_data()
print(data2)

#------------------------------------------------------------------------------

#練習9
i = 0
def A():
    i = 10
    def B():
        print(i)
    B()

A()
#B() 函式內部沒有變數 i，根據 LEGB 規則，它會向外層 A() 函式的作用域尋找。
#與UnboundLocalError差別是，錯誤發生時有「賦值」行為，而這時只有print，故依據LEGB通行

#------------------------------------------------------------------------------

#練習10
result = []
for i in range(3):
    result.append(lambda: i)
print(result)
for f in result:
    print(f(), end=" ")

#這是一個常見的閉包陷阱。lambda在被「定義」時，並沒有立刻計算i。它只是記住了要去哪裡找i(迴圈的作用域)。
#當迴圈結束後i的最終值是2。直到for f in result:迴圈中f() 被「呼叫」時，lambda才去查找 i 的值
#此時 i 已經是 2 了，所以三個函式都回傳 2

result = []
for i in range(3):
    result.append(lambda i=i: i)  # ← 關鍵！

for f in result:
    print(f(), end=" ")
