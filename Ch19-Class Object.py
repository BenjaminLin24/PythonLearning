#01
class Person:
    # 建構式，用來初始化物件的屬性
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    # 實例方法，顯示物件的資訊
    def show(self):
        print(f'姓名: {self.name}, 性別: {self.sex}, 職業: {self.profession}')

    # 實例方法，描述物件的行為
    def work(self):
        print(f'{self.name} 正在以 {self.profession} 的身份工作。')

# 建立 Person 物件 (實例化)
person1 = Person('Jessa', '女性', '軟體工程師')
person2 = Person('Jon', '男性', '醫生')

# 存取物件的屬性
print(f"第一個人的名字是: {person1.name}") # 輸出: 第一個人的名字是: Jessa

# 呼叫物件的方法
person1.show() # 輸出: 姓名: Jessa, 性別: 女性, 職業: 軟體工程師
person2.work() # 輸出: Jon 正在以 醫生的身份工作。

#class Person: 用class定義(一個名為 Person 的類別)。
#__init__(self, name, sex,...)：當Person被呼叫時會建立新物件，並作為self傳遞給 __init__，同時傳入後續的參數。
#self.name = name 將傳入的 name 值賦予給該物件的 name 屬性。
#person1 = Person(...) 創建了 Person 類別的一個實例，並將其賦值給變數 person1。
#person1.show() 透過物件呼叫其方法

#02
class Student:
    # 類別屬性，由所有 Student 物件共享
    school_name = 'ABC School'

    def __init__(self, name, age):
        # 實例屬性，每個物件獨有
        self.name = name
        self.age = age

# 建立物件
s1 = Student("Harry", 12)
s2 = Student("Emma", 13)

# 存取屬性
print(f'學生: {s1.name}, 年齡: {s1.age}, 學校: {s1.school_name}')
# 輸出: 學生: Harry, 年齡: 12, 學校: ABC School
print(f'學生: {s2.name}, 年齡: {s2.age}, 學校: {s2.school_name}')
# 輸出: 學生: Emma, 年齡: 13, 學校: ABC School

# 修改類別屬性
Student.school_name = 'XYZ School'
print("--- 學校更名後 ---")

# 所有物件共享的類別屬性值會一起改變
print(f'學生: {s1.name}, 學校: {s1.school_name}')
# 輸出: 學生: Harry, 學校: XYZ School
print(f'學生: {s2.name}, 學校: {s2.school_name}')
# 輸出: 學生: Emma, 學校: XYZ School

#類別屬性：所有物件共享，放在class下即可。也可以後續更改。
#實例屬性：屬於每個物件，通常用__init__建構式來定義

#03
#繼承(Inheritance)：一個類別(稱子類別或衍生類別)套用另一個類別(稱父類別或基底類別)的屬性和方法
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"車輛名稱: {self.name}, 最高時速: {self.max_speed}, 里程: {self.mileage}")

# 子類別 Bus 繼承自 Vehicle
class Bus(Vehicle):
    pass # pass 表示子類別目前沒有添加任何新的屬性或方法

# 建立子類別的物件
school_bus = Bus("School Volvo", 180, 12)

# 子類別物件可以直接使用父類別的方法
school_bus.display_info()
# 輸出: 車輛名稱: School Volvo, 最高時速: 180, 里程: 12

#isinstance() 是 Python 的內建函式，用來檢查一個物件是否為指定類別或其子類別的實例
print(isinstance(school_bus, Vehicle))

#04
#覆寫：可以用仔類別來修改父類別的實例屬性
#若在子類別中仍想呼叫父類別被覆寫掉的方法，可以使用 super() 函式
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        # 預設票價是座位數 * 100
        return self.capacity * 100

class Bus(Vehicle):
    # 覆寫父類別的 fare 方法
    def fare(self):
        # 使用 super() 呼叫父類別的 fare 方法取得基本票價
        base_fare = super().fare()
        # 加上 10% 的維護費
        total_fare = base_fare + (base_fare * 10 / 100)
        return total_fare

school_bus = Bus("School Volvo", 12, 50)
print("巴士總票價是:", school_bus.fare())
# 輸出: 巴士總票價是: 5500.0

#05
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子類別必須實作這個方法")

class Dog(Animal):
    def speak(self):
        return f"{self.name} 說: 汪！"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 說: 喵～"

# 建立不同類別的物件
dog = Dog("旺財")
cat = Cat("咪咪")

# 將不同物件放入一個列表中
animals = [dog, cat]

# 透過迴圈呼叫同樣的 speak 方法，但得到不同結果
for animal in animals:
    print(animal.speak())
    
#------------------------------------------------------------------------------
#範例1： 建立一個名為 Vehicle 的類別，並在建構式中接收 max_speed 和 mileage 兩個參數作為實例屬性
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

car=Vehicle(150,200)
ms=car.max_speed
print(ms)

#------------------------------------------------------------------------------
#範例2：空類別
class space:
    pass

#------------------------------------------------------------------------------
#範例3：建立一個 Book 類別，包含 title 和 author 屬性，以及一個 display 方法，可以印出 "書名 by 作者"
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def display(self):
        print(f"{self.title} by {self.author}")

tom=Book("Toms","Mark")
tom.display()

#------------------------------------------------------------------------------
#範例4：承襲第一題，增加一個color的類別屬性，預設值為"White"。
#建立兩個子類別 Bus 和 Car，並驗證它們的物件都擁有白色的屬性
class Vehicle:
    color="white"
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage


class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass

bbus=Bus(100,200)
ccar=Car(150,300)
print(bbus.color)
print(ccar.color)

#------------------------------------------------------------------------------
#範例5：建立一個 Vehicle 類別，其中有 seating_capacity 方法。
#然後建立一個 Bus 子類別，覆寫此方法，使其容量（capacity）預設為 50
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"{self.name} 的座位數是 {capacity} 人"

class Bus(Vehicle):
    # 覆寫方法並提供預設參數
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

school_bus = Bus("School Volvo", 180, 12)
print(school_bus.seating_capacity()) #產生50人，因為被複寫

#------------------------------------------------------------------------------
#範例6： 建立一個 Pet 類別，屬性包含 name, age, color。讓使用者輸入三隻寵物的資訊，存入一個列表中
#最後找出年紀最大和最小的寵物並印出其資訊
class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = int(age) # 確保年齡是整數
        self.color = color
pets = []
for i in range(3):
    name = input(f"請輸入第 {i+1} 隻寵物的名字: ")
    age = input(f"請輸入第 {i+1} 隻寵物的年齡: ")
    color = input(f"請輸入第 {i+1} 隻寵物的毛色: ")
    pets.append(Pet(name, age, color))
    print("---")

oldest_pet = max(pets, key=lambda pet: pet.age)
youngest_pet = min(pets, key=lambda pet: pet.age)

print(f"{oldest_pet.name} 是年紀最大的寵物，{oldest_pet.age} 歲。")
print(f"{youngest_pet.name} 是最年輕的寵物，{youngest_pet.age} 歲。")
# 說明: 這個練習結合了類別定義、使用者輸入、列表操作和 lambda 函式，是一個很好的綜合應用。
#max() 和 min() 函式的 key 參數可以用來指定比較的依據。

#------------------------------------------------------------------------------
#範例7：建立一個 Calculator 類別，包含 add, subtract, multiply, divide 四個方法
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "錯誤：除數不能為零"
        return x / y

sigma=Calculator()
print(sigma.divide(25,5))

#------------------------------------------------------------------------------
#範例8：建立一個 Account 類別，具有 owner 和 balance（餘額）屬性。
#提供 deposit（存款）和 withdraw（提款）方法。提款時不能透支
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"存款 {amount} 元成功。新餘額: {self.balance} 元。")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"提款失敗，餘額不足。目前餘額: {self.balance} 元。")
        else:
            self.balance -= amount
            print(f"提款 {amount} 元成功。新餘額: {self.balance} 元。")
    
    def show_balance(self):
        print(f"帳戶 {self.owner} 的目前餘額為 {self.balance} 元。")

acc1 = Account("阿昌哥")
acc1.show_balance()
acc1.deposit(1000)
acc1.withdraw(500)
acc1.withdraw(600)

#------------------------------------------------------------------------------
#範例9：建立一個 Rectangle（矩形）類別，具有 width 和 height 屬性，以及計算 area（面積）和 perimeter（周長）
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(f"矩形面積: {rect.area()}")         # 輸出: 50
print(f"矩形周長: {rect.perimeter()}")   # 輸出: 30

#------------------------------------------------------------------------------

#範例10：建立一個 Question 類別，包含 prompt（題目）和 answer（答案）屬性。
#再建立一個 Quiz 類別，可以儲存一組問題，並提供一個 run_quiz 方法來執行測驗、計分
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            user_answer = input(question.prompt + " ")
            if user_answer.lower() == question.answer.lower():
                self.score += 1
        print(f"\n測驗結束！您答對了 {self.score} / {len(self.questions)} 題。")

# 準備問題列表
question_prompts = [
    "Python 是由誰開發的？\nA) Guido van Rossum\nB) Dennis Ritchie\nC) James Gosling",
    "在 Python 中，用什麼關鍵字來定義一個類別？\nA) function\nB) def\nC) class"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c") ]

# 建立並執行測驗
my_quiz = Quiz(questions)
my_quiz.run_quiz()